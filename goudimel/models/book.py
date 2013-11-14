from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


class Book(models.Model):
    class Meta:
        app_label = "goudimel"

    title = models.CharField(max_length=255, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    published = models.DateField(blank=True, null=True)
    rism_id = models.CharField(max_length=16, blank=True, null=True)
    cesr_id = models.CharField(max_length=16, blank=True, null=True)
    remarks = models.CharField(max_length=128, blank=True, null=True)
    num_pages = models.IntegerField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"{0}".format(self.title)

@receiver(post_save, sender=Book)
def solr_index(sender, instance, created, **kwargs):
    import uuid
    from django.conf import settings
    import solr

    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:goudimel_book item_id:{0}".format(instance.id))
    if record:
        # the record already exists, so we'll remove it first.
        solrconn.delete(record.results[0]['id'])

    book = instance
    d = {
        'type': 'goudimel_book',
        'id': str(uuid.uuid4()),
        'item_id': book.id,
        'title': book.title,
        'publisher': book.publisher,
        'published': book.published,
        'rism_id': book.rism_id,
        'cesr_id': book.cesr_id,
        'remarks': book.remarks,
        'num_pages': book.num_pages,
        'created': book.created,
        'updated': book.updated
    }
    solrconn.add(**d)
    solrconn.commit()

@receiver(post_delete, sender=Book)
def solr_delete(sender, instance, created, **kwargs):
    from django.conf import settings
    import solr
    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:goudimel_book item_id:{0}".format(instance.id))
    solrconn.delete(record.results[0]['id'])
    solrconn.commit()
