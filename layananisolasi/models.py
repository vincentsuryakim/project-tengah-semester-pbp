from django.db import models

# Create your models here.
class Note(models.Model):
    untuk = models.TextField(max_length=30, default="")
    dari = models.TextField(max_length=30, default="")
    title = models.TextField(max_length=30, default="")
    message = models.TextField(max_length=30, default="")
