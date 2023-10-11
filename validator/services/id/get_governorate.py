from django.core.exceptions import ValidationError

from validator.constants import GOVERNORATE_CODES
def get_governorate(id):
    governorate_code = id[7:9]
    if governorate_code in GOVERNORATE_CODES.keys():
        return GOVERNORATE_CODES.get(governorate_code)
    else:
        raise ValidationError("Wrong Governorate")