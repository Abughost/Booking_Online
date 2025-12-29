import re

from rest_framework.exceptions import ValidationError


def normalize_phone(_phone:str):
    digits = re.findall(r'\d', _phone)
    if len(digits) < 9 or len(digits) > 12 or (9 < len(digits) < 12):
        return ValidationError('Phone number must be at least 9 digits')
    phone = "".join(_phone)
    if 9 < len(phone) and phone.startswith('998'):
        phone = phone.removeprefix('998')
    return phone

