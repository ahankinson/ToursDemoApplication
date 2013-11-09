from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


class Phrase(models.Model):
    class Meta:
        app_label = "goudimel"

    piece_id = models.ForeignKey("goudimel.Piece")
    phrase_num = models.IntegerField(blank=True, null=True)
    phrase_start = models.CharField(max_length=4, blank=True, null=True)
    phrase_stop = models.CharField(max_length=4, blank=True, null=True)
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
    record = solrconn.query("type:goudimel_phrase piece_id:{0} phrase_num:{1}".format(instance.piece_id.id, instance.phrase_num))
    if record:
        # the record already exists, so we'll remove it first.
        solrconn.delete(record.results[0]['id'])

    phrase = instance
    d = {
        'type': 'goudimel_phrase',
        'id': str(uuid.uuid4()),
        'phrase_i_piece_id': phrase.piece_id.id,
        'phrase_i_phrase_num': phrase.phrase_num,
        'phrase_s_phrase_start': phrase.phrase_start,
        'phrase_s_phrase_stop': phrase.phrase_stop,
        'phrase_s_phrase_text': phrase.phrase_text,
        'phrase_s_rhyme': phrase.rhyme,
        'phrase_d_created': phrase.created,
        'phrase_d_updated': phrase.updated
    }
    solrconn.add(**d)
    solrconn.commit()