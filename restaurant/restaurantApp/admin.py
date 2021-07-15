from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(StaffMember)
admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Booking)
admin.site.register(Table)
admin.site.register(Restaurant)