from django.db import models


class House(models.Model):
    HOUSE_MATERIAL = [
        ('crmcs', 'ceramics'),
        ('wd', 'wood')
    ]
    house_capacity = models.IntegerField()
    house_material = models.CharField(max_length=30, choices=HOUSE_MATERIAL)
    house_color = models.CharField(max_length=30)
    house_id = models.BigAutoField(primary_key=True)

