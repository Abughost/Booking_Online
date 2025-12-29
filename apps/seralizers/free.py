from rest_framework.serializers import ModelSerializer

from apps.models import User
from apps.models import Service
from apps.models.business import Appointment


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

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




