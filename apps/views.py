from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView

from apps.models import User, Service
from apps.models.business import Appointment
from apps.seralizers.free import UserModelSerializer, ServiceModelSerializer, BookingModelSerializer, \
    AppointmentModelSerializer


class MasterListAPIView(ListAPIView):
    queryset = User.objects.filter(role='master')
    serializer_class = UserModelSerializer

class MasterRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(role='master')
    serializer_class = UserModelSerializer

class ServiceListCreateAPIView(ListCreateAPIView):
    serializer_class = ServiceModelSerializer
    queryset = Service.objects.filter(status='active')

class AppointmentListCreateAPIView(ListCreateAPIView):
    queryset = Appointment.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookingModelSerializer
        return AppointmentModelSerializer

