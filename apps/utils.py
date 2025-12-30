import random
import re

from django.core.cache import cache
from pyasn1.type.univ import Boolean
from redis import Redis
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from root.settings import REDIS_HOST, REDIS_PORT


def normalize_phone(_phone:str):
    digits = re.findall(r'\d', _phone)
    if len(digits) < 9 or len(digits) > 12 or (9 < len(digits) < 12):
        return ValidationError('Phone number must be at least 9 digits')
    phone = "".join(digits)
    if 9 < len(phone) and phone.startswith('998'):
        phone = phone.removeprefix('998')
    return phone


def send_code(phone:str, expired_time=360):
    redis = Redis.from_url(f'redis://{REDIS_HOST}:{REDIS_PORT}')
    _ttl = redis.ttl(f":1:{phone}")
    if _ttl > 0:
        return False, _ttl

    code = random.randint(100_000,999_999)
    print(f"Phone : {phone} || Code : {code}")

    cache.set(phone,code,expired_time)
    return True, 0

def check_code(phone:str, code:int) -> bool:
    _code = cache.get(phone)
    if code == _code:
        cache.delete(phone)
        return True
    return False

