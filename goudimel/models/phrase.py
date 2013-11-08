from django.db import models

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