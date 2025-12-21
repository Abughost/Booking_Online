import json
import logging

from aiogram.types import Update
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from twisted.python.log import logerr

from bot import dp
from bot.config import bot

logger = logging.getLogger(__name__)

@csrf_exempt
@require_POST
async def webhook(request):
    try:
        update_data = json.loads(request.body.decode('utf-8'))
        update = Update(**update_data)
        await dp.feed_update(bot,update)
        return JsonResponse({"Status":"OK"})
    except Exception as e:
        logger.error(f"webhook xatosi {e}")
        return JsonResponse({"status": "error", "message": str(e)}, status=500)

#for checking webhook
def health_check(request):
    return HttpResponse("Django + telegram is working")



