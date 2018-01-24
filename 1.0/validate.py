def validate_zip(zipcode):
    if len(zipcode) == 6 and zipcode[2] == '-':
        try:
            int(zipcode[0:2])
            int(zipcode[-3:])
            return True
        except ValueError:
            return False
    else:
        return False

def validate_email(email):
    return False

print(validate_zip('02-125'))
print(validate_zip('1212-125'))
print(validate_zip('12125'))
print(validate_zip('1a-125'))