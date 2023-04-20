from django.db import models


class Cage(models.Model):
    CAGE_MATERIAL = [
        ('stl', 'steel'),
        ('glss', 'glass'),
        ('plstc', 'plastic')
    ]
    cage_capacity = models.IntegerField()
    cage_material = models.CharField(max_length=30, choices=CAGE_MATERIAL, null=False)
    cage_color = models.CharField(max_length=30)
    cage_id = models.BigAutoField(primary_key=True)
    gerbil_house_id = models.ForeignKey('gerbil_house.House', on_delete=models.CASCADE)



