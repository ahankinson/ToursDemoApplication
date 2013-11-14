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
    record = solrconn.query("type:goudimel_piece piece_i_id:{0}".format(instance.id))
    if record:
        # the record already exists, so we'll remove it first.
        solrconn.delete(record.results[0]['id'])

    piece = instance
    d = {
        'type': 'goudimel_piece',
        'id': str(uuid.uuid4()),
        'piece_i_id': piece.id,
        'piece_s_title': piece.title,
        'piece_s_composer_src': piece.composer_src,
        'piece_s_forces': piece.forces,
        'piece_s_print_concordances': piece.print_concordances,
        'piece_s_ms_concordances': piece.ms_concordances,
        'piece_s_pdf_link': piece.pdf_link,
        'piece_d_created': piece.created,
        'piece_d_updated': piece.updated
    }
    solrconn.add(**d)
    solrconn.commit()

@receiver(post_delete, sender=Piece)
def solr_delete(sender, instance, created, **kwargs):
    from django.conf import settings
    import solr
    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:goudimel_piece piece_i_id:{0}".format(instance.id))
    solrconn.delete(record.results[0]['id'])
    solrconn.commit()
