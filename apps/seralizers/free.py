from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, Serializer

from apps.models import Appointment, Business, Service, User
from apps.utils import normalize_phone


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'phone', 'first_name','last_name','username',

    def create(self, validated_data):
        phone = normalize_phone(validated_data['phone'])
        user, created = User.objects.get_or_create(
            phone=phone,
            defaults=validated_data)

        return user

class ChangeUserRoleSerializer(Serializer):
    role = CharField(max_length=15)

    def update(self, instance, validated_data):
        instance.role = validated_data.get('role',instance.role)
        instance.save()
        return instance

class ServiceModelSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = 'business_id','name', 'duration', 'price'

class AppointmentModelSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        exclude = 'created_at', 'updated_at'

class BusinessModelSerializer(ModelSerializer):
    class Meta:
        model = Business
        fields = "__all__"

    def create(self, validated_data):
        business, created = Business.objects.get_or_create(
            name=validated_data['name'],
            defaults=validated_data
        )

        if business:
            business.owner.add(validated_data['owner'])
            business.save()

        return business




