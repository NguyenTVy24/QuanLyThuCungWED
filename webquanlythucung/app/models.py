from django.db import models

# Create your models here.
class User(models.Model):
    idmetamaxk = models.CharField(max_length=250)

class ThuCung(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_pet = models.CharField(max_length=200)
    day_of_birth = models.DateTimeField()
    sex = models.BooleanField(default=0)
    animal_type = models.CharField(max_length=200)
    pet_image = models.ImageField(default="")