from django.db import models
# from django.urls import reverse
# Create your models here.
class Paste(models.Model):
    text = models.TextField()
    name = models.CharField(max_length=40, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name or str(self.id)

    # @permalink
    def get_absolute_url(self):
        return f'/pastebin/paste/{self.id}'