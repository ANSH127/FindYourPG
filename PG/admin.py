from django.contrib import admin
from PG.models import Userdetail,Contact,RentarDetail,multipleimage,Booking,Schedule

# Register your models here.

admin.site.register(Userdetail)
admin.site.register(Contact)
admin.site.register(RentarDetail)
admin.site.register(multipleimage)
admin.site.register(Booking)
admin.site.register(Schedule)