from rest_framework.fields import CharField, IntegerField
from rest_framework.serializers import Serializer
from rest_framework_simplejwt.tokens import RefreshToken

from apps.models import User
from apps.seralizers.free import UserModelSerializer
from apps.utils import normalize_phone


class SendCodeSerializer(Serializer):
    phone = CharField(max_length=12, default='901001010')

    def validate_phone(self, phone):
        return normalize_phone(phone)

class VerifyCodeSerializer(Serializer):
    phone = CharField(max_length=12, default='901001010')
    code = IntegerField()
    token_class = RefreshToken

    def validate_phone(self, phone):
        return normalize_phone(phone)

    def get_data(self, phone):
        user = User.objects.filter(phone=phone).first()

        if not user:
            user = User.objects.create(phone=phone)

        refresh = self.get_token(user)
        user_data = UserModelSerializer(
            user).data

        data = {
            "user" : user_data,
            'access_token' : str(refresh.access_token),
            'refresh_token' : str(refresh)
        }

        return data

    @classmethod
    def get_token(cls, user):
        return cls.token_class.for_user(user)