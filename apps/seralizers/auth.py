from rest_framework.fields import CharField
from rest_framework.serializers import Serializer


class SendCode(Serializer):
    phone = CharField(max_length=12)
