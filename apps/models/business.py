from django.db.models import SET_NULL, ManyToManyField, ForeignKey, CASCADE
from django.db.models.enums import TextChoices
from django.db.models.fields import CharField, DecimalField, FloatField, TimeField, IntegerField, DateTimeField

from apps.models import CustomUUIDBaseModel, CustomCreatedBaseModel


class Business(CustomUUIDBaseModel):
    name = CharField(max_length=255)
    owner = ManyToManyField('apps.User',SET_NULL, 'owner')

class Branch(CustomUUIDBaseModel):
    name = CharField(max_length=255)
    business = ForeignKey('apps.Business',CASCADE, 'business')
    latitude =  FloatField(max_length=10)
    longitude = FloatField(max_length=10)

class Service(CustomCreatedBaseModel):
    business = ForeignKey('apps.Business',CASCADE, 'business')
    duration = TimeField()
    price = IntegerField()


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
        ordering = '-start-time'

    def save(self, *args, **kwargs):
        if self.service and not self.end_time:
            from datetime import timedelta
            self.end_time = self.start_time + timedelta(minutes=self.service.duration)



