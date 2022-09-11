from django.db import models


class Gerbil(models.Mode):

    GERBIL_COLOR = (
        ('WH', 'white'),
        ('GD', 'gold'),
        ('BLCK', 'black'),
        ('GR', 'grey'),
        ('BN', 'brown')
    )

    GERBIL_SEX = (
        ('f', 'female'),
        ('m', 'male')
    )
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=1, choices=GERBIL_COLOR)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=GERBIL_SEX)