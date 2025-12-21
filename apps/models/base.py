import uuid

from django.db.models import Func, Model
from django.db.models.fields import UUIDField, DateTimeField


class GenRandomUUID(Func):
    function = 'gen_random_uuid'
    template = '%(function)s()'
    output_fields = UUIDField()

class CustomUUIDBaseModel(Model):
    id = UUIDField(
        primary_key=True,
        db_default=GenRandomUUID(),
        default=uuid.uuid4(),
        editable=False
    )

    class Meta:
        abstract=True

class CustomCreatedBaseModel(CustomUUIDBaseModel):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True

