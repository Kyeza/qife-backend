def get_international_phone_number_format(phone_number):
    if phone_number.startswith("+256"):
        return phone_number
    elif phone_number.startswith("256"):
        return f'+{phone_number}'
    elif phone_number.startswith("0"):
        return f'+256{phone_number[1:]}'
    else:
        return None
