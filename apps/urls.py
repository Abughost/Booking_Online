from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.views.auth import SendCodeApiView, VerifyCodeApiView
from apps.views.views import (AppointmentModelViewSet, BusinessListCreateAPIView,
                        ClientListCreateAPIView,
                        ClientRetrieveUpdateDestroyAPIView,
                        MasterListCreateAPIView,
                        MasterRetrieveUpdateDestroyAPIView,
                        ServiceModelViewSet)

router = DefaultRouter()
router.register('appointment', AppointmentModelViewSet)
router.register('service',ServiceModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('send-code', SendCodeApiView.as_view(), name='send_code'),
    path('varify-code', VerifyCodeApiView.as_view(), name='verify_code'),
    path('masters', MasterListCreateAPIView.as_view(), name='masters'),
    path('master/<int:uuid>', MasterRetrieveUpdateDestroyAPIView.as_view(), name='master_retrieve'),
    path('client', ClientListCreateAPIView.as_view(),name='clients'),
    path('client/<int:uuid>', ClientRetrieveUpdateDestroyAPIView.as_view(),name='client_retrieve'),
    path('business', BusinessListCreateAPIView.as_view(), name='business'),
]