from django.core.exceptions import ValidationError
import re

def validate_iranian_cellphone_number(value):
    pattern = r'^0\d{10}$'
    if not re.match(pattern, value):
        raise ValidationError('لطفا یک شماره تلفن معتبر وارد کنید')