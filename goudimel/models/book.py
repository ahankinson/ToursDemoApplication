from django.db import models

class Book(models.Model):
    class Meta:
        app_label = "goudimel"

    title = models.CharField(max_length=255, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    published = models.DateField(blank=True, null=True)
    rism_id = models.CharField(max_length=16, blank=True, null=True)
    cesr_id = models.CharField(max_length=16, blank=True, null=True)
    remarks = models.CharField(max_length=128, blank=True, null=True)
    num_pages = models.CharField(max_length=16, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"{0}".format(self.title)