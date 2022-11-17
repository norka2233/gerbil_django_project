from django.db import models


class House(models.Model):

    HOUSE_MATERIAL = [
        ('CR', 'ceramics'),
        ('WD', 'wood')
    ]

    capacity = models.IntegerField()
    material = models.CharField(max_length=30, choices=HOUSE_MATERIAL)


