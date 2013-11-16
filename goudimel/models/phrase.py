from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


class Phrase(models.Model):
    class Meta:
        app_label = "goudimel"

    piece_id = models.ForeignKey("goudimel.Piece")
    phrase_num = models.IntegerField(blank=True, null=True)
    phrase_start = models.IntegerField(blank=True, null=True)
    phrase_stop = models.IntegerField(blank=True, null=True)
    phrase_text = models.CharField(max_length=255, blank=True, null=True)
    rhyme = models.CharField(max_length=64, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"{0}".format(self.phrase_text)

@receiver(post_save, sender=Phrase)
def solr_index(sender, instance, created, **kwargs):
    import uuid
    from django.conf import settings
    import solr

    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:goudimel_phrase item_id:{0}".format(instance.id))
    if record:
        # the record already exists, so we'll remove it first.
        solrconn.delete(record.results[0]['id'])

    phrase = instance
    d = {
        'type': 'goudimel_phrase',
        'id': str(uuid.uuid4()),
        'item_id': phrase.id,
        'phrase_num': phrase.phrase_num,
        'phrase_start': phrase.phrase_start,
        'phrase_stop': phrase.phrase_stop,
        'phrase_text': phrase.phrase_text,
        'rhyme': phrase.rhyme,
        'created': phrase.created,
        'updated': phrase.updated
    }
    solrconn.add(**d)
    solrconn.commit()

@receiver(post_delete, sender=Phrase)
def solr_delete(sender, instance, created, **kwargs):
    from django.conf import settings
    import solr
    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:goudimel_phrase item_id:{0}".format(instance.id))
    solrconn.delete(record.results[0]['id'])
    solrconn.commit()
