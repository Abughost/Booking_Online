from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import action, permission_classes
from rest_framework.generics import (ListCreateAPIView, UpdateAPIView, RetrieveUpdateAPIView)
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.models import Appointment, Business, Service, User
from apps.permissions import IsOwnerOrReadOnly
from apps.seralizers import (AppointmentModelSerializer,
                             BusinessModelSerializer, ServiceModelSerializer,
                             UserModelSerializer)
from apps.seralizers.free import ChangeUserRoleSerializer


@extend_schema(tags=['User'])
class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'change_role':
            return ChangeUserRoleSerializer
        return UserModelSerializer

    @action(['patch'],True,'role', permission_classes=[IsOwnerOrReadOnly])
    def change_role(self, request, pk=None):
        user = self.get_object()
        new_role = request.data.get('role')

        if new_role not in ['owner', 'client', 'employee']:
            return Response({"error": 'wrong role'}, status.HTTP_400_BAD_REQUEST)
        user.role = new_role
        user.save()
        return Response({
            'user': user,
            'message':'Role changed successfully',
            'role':new_role
        }, status.HTTP_202_ACCEPTED)


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

