from django.contrib import admin

from .models import Shop, Employee, Service, ServiceFromEmployee, Rating

admin.site.register(Shop)
admin.site.register(Employee)
admin.site.register(Service)
admin.site.register(ServiceFromEmployee)
admin.site.register(Rating)

