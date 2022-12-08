from django.db import models
from django.urls import reverse

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    #solving the get_absolute_url error that comes when a new object is created but does not get saved anywhere : use reserse()
    def get_absolute_url(self):
        return reverse("publishers:publisherdetail", kwargs ={"id":self.id})


    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

