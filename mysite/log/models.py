from django.db import models
from django.contrib.auth.models import User

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 50)
    img_url = models.CharField(max_length = 250)
    time = models.CharField(max_length = 100)
    