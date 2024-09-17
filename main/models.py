from django.db import models
import uuid  



class Hat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 225)
    desc = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.CharField(max_length=22083)