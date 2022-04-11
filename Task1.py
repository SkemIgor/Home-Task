import re

EMAIL = re.compile(r'(^[a-z0-9_\.-]+)@([a-z0-9]+\.[a-z]+)')

def email_parse(email_address):
    email = EMAIL.findall(email_address)
    if email:
        login, domen = email[0]
    else:
        raise ValueError(f'wrong email: {email_address}')
    print(login, domen)

email_parse('skemigor@mail.ru')
email_parse('skemigor@@mail.ru')