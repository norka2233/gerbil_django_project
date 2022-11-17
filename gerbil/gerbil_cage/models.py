from django.db import models

class Cage(models.Model):

    CAGE_MATERIAL = [
        ('ST', 'steel'),
        ('GL', 'glass'),
        ('PL', 'plastic')
    ]

    capacity = models.IntegerField()
    material = models.CharField(max_length=30, choices=CAGE_MATERIAL)
    color = models.CharField(max_length=30)