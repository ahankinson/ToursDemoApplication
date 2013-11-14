from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


class Piece(models.Model):
    class Meta:
        app_label = "goudimel"

    book_id = models.ForeignKey("goudimel.Book")
    title = models.CharField(max_length=64, blank=True, null=True)
    composer_src = models.CharField(max_length=64, blank=True, null=True)
    forces = models.CharField(max_length=16, blank=True, null=True)
    print_concordances = models.CharField(max_length=128, blank=True, null=True)
    ms_concordances = models.CharField(max_length=128, blank=True, null=True)
    pdf_link = models.URLField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u"{0}".format(self.title)

    @property
    def composer_name(self):
        name = self.composer_src.split(",")
        if len(name) > 1:
            return u"{0} {1}".format(name[1], name[0])
        else:
            return u"{0}".format(self.composer_src)


@receiver(post_save, sender=Piece)
def solr_index(sender, instance, created, **kwargs):
    import uuid
    from django.conf import settings
    import solr

    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:goudimel_piece item_id:{0}".format(instance.id))
    if record:
        # the record already exists, so we'll remove it first.
        solrconn.delete(record.results[0]['id'])

    piece = instance
    d = {
        'type': 'goudimel_piece',
        'id': str(uuid.uuid4()),
        'item_id': piece.id,
        'title': piece.title,
        'composer_src': piece.composer_src,
        'forces': piece.forces,
        'print_concordances': piece.print_concordances,
        'ms_concordances': piece.ms_concordances,
        'pdf_link': piece.pdf_link,
        'created': piece.created,
        'updated': piece.updated
    }
    solrconn.add(**d)
    solrconn.commit()

@receiver(post_delete, sender=Piece)
def solr_delete(sender, instance, created, **kwargs):
    from django.conf import settings
    import solr
    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:goudimel_piece item_id:{0}".format(instance.id))
    solrconn.delete(record.results[0]['id'])
    solrconn.commit()
