from django.urls import path, include

from apps.views import MasterListApiView

urlpatterns = [
    path('masters', MasterListApiView.as_view()),
]