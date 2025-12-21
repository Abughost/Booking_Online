from django.urls import path

from apps.views import MasterListApiView, telegram_webhook

urlpatterns = [
    path('masters', MasterListApiView.as_view()),
]