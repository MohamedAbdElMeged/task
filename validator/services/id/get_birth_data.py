from datetime import datetime
from django.core.exceptions import ValidationError

def get_birth_date(id):
    century = '19' if id[0] == '2' else '20'
    year = "{}{}".format(century,id[1:3]) 
    month = id[3:5]
    day = id[5:7]
    birth_date =  "{}-{}-{}".format(year,month,day)
    try:
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
    except:
        raise ValidationError("Invalid Birth Date format")
    current_date = datetime.now().date()
    if birth_date > current_date:
        raise ValidationError("Birth date shouldn't be in the future")
    return birth_date

