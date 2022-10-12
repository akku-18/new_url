from email.policy import default
from django.db import models

# Create your models here.
class SURL(models.Model):
    link = models.CharField(max_length = 10000)
    uuid = models.CharField(max_length = 10)
    urldic = models.CharField(max_length=100, default="nothing")


