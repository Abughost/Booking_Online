from rest_framework.serializers import ModelSerializer

from apps.models import User


class MasterModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'





