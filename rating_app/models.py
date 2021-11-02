from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Shop(models.Model):
    """A Shop where the user later will rate services"""
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'owner'], name='owner_unique_shop')
        ]

    def __str__(self):
        """Return a string representation of the Shop."""
        return f'{self.name}'


class Rating(models.Model):
    """Rate a Service at a Shop from an Employee"""
    id = models.IntegerField(primary_key=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    description = models.TextField()
    rating = models.IntegerField(default = 0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'ratings'

    def __str__(self):
        return f'({self.rating}) {self.description[:80]}'