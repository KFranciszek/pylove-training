import re
def validate_email(email):
    pat = ''
    if re.match(pat,email):
        return True
    else:
        return False

def validate_code(postal_code):
    pat = ''
    if re.match(pat,code):
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