from django.db import models

# Create your models here.


# class MoodEntry(models.Model):
#     mood = models.CharField(max_length=255)
#     time = models.DateField(auto_now_add=True)
#     feelings = models.TextField()
#     mood_intensity = models.IntegerField()

#     @property
#     def is_mood_strong(self):
#         return self.mood_intensity > 5
    


class Hat(models.Model):
    name = models.CharField(max_length = 225)
    desc = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.CharField(max_length=22083)