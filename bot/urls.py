from django.urls import path

from bot.view import webhook, health_check

urlpatterns=[
    path('webhook/', webhook, name='webhook'),
    path('health', health_check, name='health')
]