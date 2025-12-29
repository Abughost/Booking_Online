from django.urls import path

from bot.view import health_check, webhook

urlpatterns=[
    path('webhook/', webhook, name='webhook'),
    path('health', health_check, name='health')
]