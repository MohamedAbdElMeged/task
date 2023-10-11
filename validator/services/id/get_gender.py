def get_gender(id):
    gender_number= int(id[9:13])
    if gender_number % 2 == 0:
        return "Female"
    else:
        return "Male"