from django.contrib.auth.models import AbstractUser
from django.db.models.enums import TextChoices
from django.db.models.fields import CharField

from apps.models import CustomCreatedBaseModel


class User(AbstractUser ,CustomCreatedBaseModel):
    class RoleType(TextChoices):
        owner = 'owner', 'Owner'
        client = 'client', 'Client'
        Employee = 'employee','Employee'

    phone = CharField(max_length=15, unique=True)
    role = CharField(max_length=10, choices=RoleType, default=RoleType.client)

    email = None
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

