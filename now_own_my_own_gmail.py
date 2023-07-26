import re

def is_valid_mail(mail_address):
    if not (isinstance(mail_address, str)):
        return False

    # Pattern email
    pattern = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    # Check For Matches
    match = re.match(pattern,mail_address )

    if match:
        return True
    else:
        return False

# test now_own_my_own_gmail.py
mail1 = "example@gmail.com"
mail2 = "bad_mail@.com"
mail3 = "anotherexample@domain.com"
mail4 = "wrong_mail@@gmail.com"
mails = {mail1, mail2, mail3, mail4}

for mail in mails:
    print(f'This is the mail: {mail}')
    print(f'Is this a valid mail: {is_valid_mail(mail)}\n')

