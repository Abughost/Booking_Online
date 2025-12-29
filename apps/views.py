from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from apps.models import User, Service
from apps.models.business import Appointment
from apps.seralizers.free import UserModelSerializer, ServiceModelSerializer, BookingModelSerializer, \
    AppointmentModelSerializer
from apps.utils import normalize_phone


class MasterListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.filter(role='master')
    serializer_class = UserModelSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(role='master')

        return Response(serializer.data, status.HTTP_201_CREATED)


class MasterRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(role='master')
    serializer_class = UserModelSerializer


class ClientListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.filter(role='client')
    serializer_class = UserModelSerializer

class ClientRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(role='client')
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

class AppointmentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentModelSerializer



