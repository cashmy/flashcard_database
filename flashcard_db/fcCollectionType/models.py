from django.db import models


# Create your models here.
class FcCollectionType(models.Model):
    fcCollectionType_id = models.CharField(max_length=2, primary_key=True, unique=True)
    fcCollectionType_name = models.CharField(max_length=50, null=False, blank=False)
    fcCollectionType_desc = models.CharField(max_length=250, null=False, blank=True)
    # fcCollectionType_audioFileUrl = models.FileField(max_length=250, null=True, blank=True)
    # fcCollectionType_videoFileUrl = models.FileField(max_length=250, null=True, blank=True)
    # fcCollectionType_imageFileUrl = models.ImageField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.fcCollectionType_name
