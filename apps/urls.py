from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.views import (AppointmentModelViewSet, BusinessListCreateAPIView, SendCodeApiView,
                        ServiceModelViewSet, VerifyCodeApiView)
from apps.views.views import UserModelViewSet

router = DefaultRouter()
router.register('appointment', AppointmentModelViewSet)
router.register('service',ServiceModelViewSet)
router.register('User', UserModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('send-code', SendCodeApiView.as_view(), name='send_code'),
    path('varify-code', VerifyCodeApiView.as_view(), name='verify_code'),
    path('business', BusinessListCreateAPIView.as_view(), name='business'),
]