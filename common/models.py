from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Region(BaseModel):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class District(BaseModel):
    name = models.CharField(max_length=64)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class SubCategory(BaseModel):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Manufacturer(BaseModel):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
