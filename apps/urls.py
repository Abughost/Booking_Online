from django.urls import path

from apps.views import MasterListCreateAPIView, ServiceListCreateAPIView, AppointmentListCreateAPIView, \
    MasterRetrieveUpdateDestroyAPIView, ClientListCreateAPIView, ClientRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('masters', MasterListCreateAPIView.as_view(), name='masters'),
    path('master/<int:uuid>', MasterRetrieveUpdateDestroyAPIView.as_view(), name='master_retrieve'),
    path('client', ClientListCreateAPIView.as_view(),name='clients'),
    path('client/<int:uuid>', ClientRetrieveUpdateDestroyAPIView.as_view(),name='client_retrieve'),
    path('service', ServiceListCreateAPIView.as_view(), name='services'),
    path('appointment', AppointmentListCreateAPIView.as_view(), name='appointment'),
]