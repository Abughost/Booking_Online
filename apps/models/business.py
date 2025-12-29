from django.db.models import CASCADE, SET_NULL, ForeignKey, ManyToManyField
from django.db.models.enums import TextChoices
from django.db.models.fields import (CharField, DateTimeField, DecimalField,
                                     FloatField, IntegerField, TimeField)

from apps.models import CustomCreatedBaseModel, CustomUUIDBaseModel


class Business(CustomUUIDBaseModel):
    name = CharField(max_length=255)
    owner = ManyToManyField('apps.User','businesses')

class Branch(CustomUUIDBaseModel):
    name = CharField(max_length=255)
    business = ForeignKey('apps.Business',CASCADE, 'branch')
    latitude =  FloatField(max_length=10)
    longitude = FloatField(max_length=10)

class Service(CustomCreatedBaseModel):
    class ServiceStatus(TextChoices):
        active = 'active', 'Active'
        inactive = 'inactive', 'Inactive'

    business = ForeignKey('apps.Business',CASCADE, 'service')
    name = CharField(max_length=255)
    duration = TimeField()
    price = IntegerField()
    status =CharField(max_length=10, choices=ServiceStatus, default=ServiceStatus.active)


class Appointment(CustomCreatedBaseModel):
    class AppStatus(TextChoices):
        in_process = 'in_process', 'In_process'
        confirmed = 'confirmed', 'Confirmed'
        completed = 'completed', 'Completed'
        cancelled = 'cancelled', 'Cancelled'

    service = ForeignKey('apps.Service',CASCADE, 'service')
    master = ForeignKey('apps.User',CASCADE, 'master')
    client = ForeignKey('apps.User',CASCADE, 'client')
    start_time = DateTimeField()
    end_time = DateTimeField(editable=False)
    status = CharField(max_length=12,choices=AppStatus, default=AppStatus.confirmed)

    class Meta:
        ordering = '-start_time',

    def save(self, *args, **kwargs):
        if self.service and not self.end_time:
            from datetime import timedelta
            self.end_time = self.start_time + timedelta(minutes=self.service.duration)



