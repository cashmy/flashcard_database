from django.db import models


# Create your models here.
class FcCollectionType(models.Model):
    fcCollectionType_id = models.CharField(max_length=2, primary_key=True, unique=True)
    fcCollectionType_name = models.CharField(max_length=50, null=False, blank=False)
    fcCollectionType_desc = models.CharField(max_length=250, null=False, blank=True)

    def __str__(self):
        return self.fcCollectionType_name
