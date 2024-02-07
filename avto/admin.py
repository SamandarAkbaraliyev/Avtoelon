from django.contrib import admin
from avto.models import CarAnnouncement, Leasing, Contact


admin.site.register([CarAnnouncement, Leasing, Contact])
