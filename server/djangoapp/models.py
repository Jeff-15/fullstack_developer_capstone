# Uncomment the following imports before adding the Model code

from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

class CarMake(models.Model):
    name = models.CharField(null=False,max_length=50,default="somemaker")
    description = models.CharField(max_length=1000)
    def __str__(self) -> str:
        return "Name: "+self.name+", Description: "+self.description


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

class CarModel(models.Model):
    name = models.CharField(null=False,max_length=50,default="somemaker")
    VALIDATORS = [
        MaxValueValidator(2023),
        MinValueValidator(2015)
    ]
    year = models.IntegerField(null=False,validators=VALIDATORS,default=2019)
    description = models.CharField(max_length=1000)
    SEDAN = "Sedan"
    SUV = "SUV"
    WAGON = "Wagon"
    PC = "People carrier"
    COUPE = "Coupe"
    TYPECHOICE = [
        (SEDAN,"sedan"),
        (SUV,"SUV"),
        (WAGON,"wagon"),
        (PC,"people carrier"),
        (COUPE, "coupe"),
    ]
    type = models.CharField(null=False,max_length=30,choices=TYPECHOICE,default=WAGON)
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return "Name: "+self.name+", Make: "+self.make.name+"Type: "+self.type
