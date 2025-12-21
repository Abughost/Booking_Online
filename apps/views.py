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

@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        try:
            # 1. Kelgan ma'lumotni dekod qilish
            update = ujson.load(request.body.decode('utf-8'))


            # 2. Aiogram Update obyektiga aylantirish
            update = types.Update(**update)

            # 3. Asinxron loopni olish yoki yaratish
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            # 4. Xabarni qayta ishlash
            loop.run_until_complete(dp.feed_update(bot, update))
            loop.close()

            return HttpResponse(status=200)
        except Exception as e:
            print(f"Webhook xatosi: {e}")
            return HttpResponse(status=500)

    return HttpResponse("Faqat POST so'rovlar!", status=400)