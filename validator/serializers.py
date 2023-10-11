from django.core.exceptions import ValidationError

def validate_id(data):
    id = data.get('id', None)
    _validate_presence(id)
    _validate_length(id)
    _validate_no_spaces(id)
    _validate_is_numeric(id)
    _validate_century(id)
    _validate_month(id)

def _validate_presence(id):
    if not id:
        raise ValidationError("id can't be blank")
    return True

def _validate_length(id):
    if len(id) < 14:
        raise ValidationError("id length should be 14 numbers")
    return True

def _validate_is_numeric(id):
    if not id.isdigit():
        raise ValidationError("id should contain numbers only")
    return True

def _validate_no_spaces(id):
    if ' ' in id:
        raise ValidationError("id shouldn't contain spaces")
    return True

def _validate_century(id):
    if id[0] != '2' and id[0] != '3':
        raise ValidationError("id should start with 2 or 3")
    return True

def _validate_month(id):
    month = int(id[3:5])
    if month > 12 or month < 1:
        raise ValidationError("Month should be between 1 and 12")
    return True
