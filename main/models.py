import uuid  
from django.db import models
from django.contrib.auth.models import User


class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    product = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    desc = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.CharField(max_length=22083) 

    


# class Hat(models.Model):
#     name = models.CharField(max_length = 225)
#     desc = models.TextField()
#     price = models.IntegerField()
#     stock = models.IntegerField()
#     image = models.CharField(max_length=22083)