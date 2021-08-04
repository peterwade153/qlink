import datetime

import jwt
from django.conf import settings
from django.db import IntegrityError
from authentication.models import TokenBlacklist


def generate_access_token(user):
    exp_time = datetime.datetime.now() + datetime.timedelta(
        hours=settings.AUTH_TOKEN_EXPIRE_HOURS
    )
    payload = {
        "email": user.email,
        "exp": exp_time
    }
    token = jwt.encode(
        payload, 
        settings.SECRET_KEY, 
        algorithm="HS256"
    ).decode('utf-8')
    return token

def blacklist_access_token(token):
    try:
        TokenBlacklist.objects.create(token=token)
    except IntegrityError:
        pass
    return
