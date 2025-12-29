from django.urls import path

from apps.views import MasterListAPIView, ServiceListCreateAPIView, AppointmentListCreateAPIView, \
    MasterRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('masters', MasterListAPIView.as_view(), name='masters'),
    path('master/<int:uuid>', MasterRetrieveUpdateDestroyAPIView.as_view(), name='master_retrieve'),
    path('service', ServiceListCreateAPIView.as_view(), name='services'),
    path('appointment', AppointmentListCreateAPIView.as_view(), name='appointment'),
]