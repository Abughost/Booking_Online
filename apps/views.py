import asyncio
import json
import types

import ujson
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView

from apps.models import User
from apps.seralizers.free import MasterModelSerializer
from bot import dp
from bot.config import bot


class MasterListApiView(ListAPIView):
    serializer_class = MasterModelSerializer
    queryset = User.objects.filter(role='master')
