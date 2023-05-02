from django.db import models
from django.db import models, IntegrityError, DataError



class Gerbil(models.Model):
    GERBIL_COLOR_CHOICES = [
        ('wht', 'white'),
        ('gld', 'gold'),
        ('blck', 'black'),
        ('gr', 'grey'),
        ('brw', 'brown'),
        ('N/A', 'not indiated')
    ]
    gerbil_name = models.CharField(max_length=30, null=False)
    gerbil_age = models.IntegerField(null=False)
    gerbil_id = models.BigAutoField(primary_key=True)
    gerbil_color = models.CharField(choices=GERBIL_COLOR_CHOICES, max_length=5, null=False, default='N/A')
    gerbil_cage_id = models.ForeignKey('gerbil_cage.Cage', on_delete=models.CASCADE)
    gerbil_house_id = models.ForeignKey('gerbil_house.House', on_delete=models.CASCADE)
    # gerbil_sex = models.TextChoices('male', 'female')

    # @staticmethod
    # def add_gerbil(gerbil_name, gerbil_id, gerbil_age, gerbil_color, gerbil_cage_id, gerbil_house_id):
    #     gerbil = Gerbil(gerbil_name=gerbil_name, gerbil_id=gerbil_id, gerbil_age=gerbil_age, gerbil_color=gerbil_color, gerbil_cage_id=gerbil_cage_id, gerbil_house_id=gerbil_house_id)
    #     try:
    #         gerbil.save()
    #         return gerbil
    #     except (IntegrityError, AttributeError, DataError):
    #         pass


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

