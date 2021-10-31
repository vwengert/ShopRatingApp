from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Shop(models.Model):
    """A Shop where the user later will rate services"""
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        """Return a string representation of the Shop."""
        return f'{self.name}: {self.description}'

class Employee(models.Model):
    """An Employee who is responsible for the service you rate"""
    id = models.IntegerField(primary_key=True)
    shopId = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'employees'

    def __str__(self):
        """Return a string of the Employee"""
        return self.name

class Service(models.Model):
    """A Service which get offered at a shop"""
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'services'

    def __str__(self):
        """Return a string of the service"""
        return f'{self.name}: {self.description}'

class ServiceFromEmployee(models.Model):
    """A Service offered by an Employee in a shop"""
    id = models.IntegerField(primary_key=True)
    employeeId = models.ForeignKey(Employee, on_delete=models.CASCADE)
    serviceId = models.ForeignKey(Service, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'servicesFromEmployees'

    def __str__(self):
        return f'{self.id} {self.employeeId} {self.serviceId}'

class Rating(models.Model):
    """Rate a Service at a Shop from an Employee"""
    id = models.IntegerField(primary_key=True)
    serviceFromEmployeeId = models.ForeignKey(ServiceFromEmployee, on_delete=models.CASCADE)
    rating = models.IntegerField(default = 0, validators=[MaxValueValidator(5), MinValueValidator(0)])

    class Meta:
        verbose_name_plural = 'ratings'

    def __str__(self):
        return f'{self.rating}'