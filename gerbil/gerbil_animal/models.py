from django.db import models


class Gerbil(models.Model):

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
    color = models.CharField(max_length=5, choices=GERBIL_COLOR)
    age = models.IntegerField()
    sex = models.CharField(max_length=2, choices=GERBIL_SEX)
    id = models.BigAutoField(primary_key=True)

    def eat(self):
        return "Gerbil eats"

    def run(self):
        return "Gerbil Runs"

    def groom(self):
        return "Gerbil Grooms"

    def poo(self):
        return "Gerbil Poos"

    def drink(self):
        return "Gerbil Drinks"

    def sleep(self):
        return "Gerbil Sleeps"

    def die(self):
        return "Gerbil Dies"

    def born(self):
        return "Gerbil Borns"

    def gnaw(self):
        return "Gerbil Gnaws"

    def peck(self):
        return "Gerbil Pecks"

