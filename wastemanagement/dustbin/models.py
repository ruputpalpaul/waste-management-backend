from django.db import models


class Dustbin(models.Model):
    id = models.AutoField(primary_key=True)
    station_id = models.IntegerField(null=False)
    location = models.CharField(max_length=255)
