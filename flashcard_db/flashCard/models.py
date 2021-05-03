from django.db import models


# Create your models here.
class FlashCard(models.Model):
    fcCollection_id = models.ForeignKey('fcCollections.FcCollection', on_delete=models.CASCADE)
    face = models.CharField(max_length=250, null=False, blank=True)
    back = models.CharField(max_length=250, null=False, blank=True)

    def __str__(self):
        return 'Card: ' + self.face
