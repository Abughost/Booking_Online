from drf_spectacular.utils import extend_schema
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.viewsets import ModelViewSet

from apps.models import Appointment, Business, Service, User
from apps.seralizers import (AppointmentModelSerializer,
                             BusinessModelSerializer, ServiceModelSerializer,
                             UserModelSerializer)


class MasterListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.filter(role='master')
    serializer_class = UserModelSerializer

    def perform_create(self, serializer):
        serializer.save(role='master')

class MasterRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(role='master')
    serializer_class = UserModelSerializer

class ClientListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.filter(role='client')
    serializer_class = UserModelSerializer

    def perform_create(self, serializer):
        serializer.save(role='client')

class ClientRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(role='client')
    serializer_class = UserModelSerializer

@extend_schema(tags=['Service'])
class ServiceModelViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceModelSerializer

@extend_schema(tags=['Appointment'])
class AppointmentModelViewSet(ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentModelSerializer

class BusinessListCreateAPIView(ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessModelSerializer

