from django.db import models  # pyright: ignore[reportMissingModuleSource]

class shop(models.Model):
    ism_familya = models.CharField(max_length=255)
    shikoyat_turi = models.IntegerField()
    prablema = models.CharField(max_length=255)
