from django.db import models

# Create your models here.


class TVShow(models.Model):

    name = models.CharField(max_length=256, null=True)

