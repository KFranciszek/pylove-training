def validate_email(email):
    dot = (email[-3] == '.')
    dot2 = (email[-4] == '.')
    amper = '@' in email
    if (dot or dot2) and amper:
        return True
    else:
        return False

def is_digit(numb):
    try:
        if int(numb) in [0,1,2,3,4,5,6,7,8,9]:
            return True
        else:
            return False
    except:
        return False

def validate_code(postal_code):
    code = list(postal_code)
    if len(postal_code) != 6:
        return False
    if is_digit(code[0]) and is_digit(code[1]) and code[2] == '-' and is_digit(code[3]) and is_digit(code[4]):
        return True
    else:
        return False

print(validate_email('piotr@dyba.pl'))
print(validate_email('piotr@dyba.com'))
print(validate_email('piotr@dyba'))
print(validate_email('piotrdyba.com.pl'))
print(validate_code('61-287'))
print(validate_code('61-2v7'))
print(validate_code('61287'))
print(validate_code('6f-287'))
print(validate_code('6156-287'))