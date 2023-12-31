from django.db import models

# Create your models here.
class User(models.Model):
    idmetamaxk = models.CharField(max_length=250)

class ThuCung(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hop_dong = models.CharField(max_length=200,default="")
    name_pet = models.CharField(max_length=200,default="")
    day_of_birth = models.DateTimeField()
    sex = models.BooleanField(default=0)
    animal_type = models.CharField(max_length=200,default="")
    pet_image = models.ImageField(default="")
    father = models.CharField(max_length=10,default="")
    mother = models.CharField(max_length=10,default="")
    def __str__(self):
        return self.name_pet