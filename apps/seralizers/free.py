from rest_framework.serializers import ModelSerializer

from apps.models import User
from apps.models import Service
from apps.models.business import Appointment
from apps.utils import normalize_phone


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'phone', 'first_name','last_name','username',

    def create(self, validated_data):
        validated_data["phone"] = normalize_phone(validated_data['phone'])
        user, created = User.objects.get_or_create(
            defaults=validated_data)

        if created:
            user.save()
        return user



class ServiceModelSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = 'name', 'duration', 'price'

class BookingModelSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = 'service', 'master', 'start_time'

class AppointmentModelSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        exclude = 'created_at', 'updated_at'




