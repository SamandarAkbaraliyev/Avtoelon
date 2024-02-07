from django.db import models
from common.models import (
    BaseModel,
    SubCategory,
    Manufacturer,
    Region,
    District,
)
from avto import constants
from multiselectfield import MultiSelectField


class CarModel(BaseModel):
    name = models.CharField(max_length=32)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Position(BaseModel):
    name = models.CharField(max_length=32)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CarAnnouncement(BaseModel):
    model_of_car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    kuzov = models.CharField(max_length=32, choices=constants.Kuzov.choices, default=constants.Kuzov.SEDAN)

    price = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    manufactured_year = models.DateField()
    has_bargain = models.BooleanField(default=False)
    has_leasing = models.BooleanField(default=False)

    engine_capacity = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    fuel_type = models.CharField(max_length=16, choices=constants.FuelType.choices)
    gearbox = models.CharField(max_length=16, choices=constants.Gearbox.choices)

    kilometers = models.DecimalField(max_digits=16, decimal_places=3, null=True, blank=True)
    color = models.CharField(max_length=32, choices=constants.Color.choices, null=True, blank=True)
    color_condition = models.CharField(max_length=32, choices=constants.ColorCondition.choices, null=True, blank=True)

    gear = models.CharField(max_length=16, choices=constants.Gear.choices, null=True, blank=True)
    outer_side = MultiSelectField(choices=constants.Outer.choices, null=True, blank=True, max_length=32)
    optika = MultiSelectField(choices=constants.Optika.choices, null=True, blank=True, max_length=32)

    salon = MultiSelectField(choices=constants.Salon.choices, null=True, blank=True, max_length=32)
    additional_features = MultiSelectField(
        choices=constants.AdditionalFeatures.choices, null=True, blank=True, max_length=32)
    additional_info = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='avto/')

    def __str__(self):
        return self.name


class Leasing(BaseModel):
    payment_for_beginning = models.IntegerField(default=0)
    months = models.IntegerField(default=0)
    payment_per_months = models.IntegerField(default=0)
    car = models.ForeignKey(CarAnnouncement, on_delete=models.CASCADE)

    def __str__(self):
        return f"Leasing for {self.car}"


class Contact(BaseModel):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=16)
    car = models.ForeignKey(CarAnnouncement, on_delete=models.CASCADE)


class MotoMarka(BaseModel):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name
