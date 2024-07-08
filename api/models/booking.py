import phonenumbers
from django.db import models

from api.models import Service, CompanyLocation


class Booking(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()

    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    office = models.ForeignKey(CompanyLocation, on_delete=models.CASCADE)

    def __str__(self):
        return f'<Booking {self.name}>'
