from django.db import models


# Create your models here.
class FcCollection(models.Model):
    fcCollection_id = models.AutoField(primary_key=True, unique=True)
    fcCollection_title = models.CharField(max_length=50, null=False, blank=True)
    fcCollection_type_id = models.ForeignKey('fcCollectionType.FcCollectionType', on_delete=models.CASCADE)

    def __str__(self):
        return self.fcCollection_title
