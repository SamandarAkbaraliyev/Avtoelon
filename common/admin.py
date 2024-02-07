from django.contrib import admin
from common.models import (
    Region,
    District,
    Category,
    SubCategory,
    Manufacturer,
)


admin.site.register([Region, District, Category, SubCategory, Manufacturer])
