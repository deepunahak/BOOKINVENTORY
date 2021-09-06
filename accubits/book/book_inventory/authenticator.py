from django.core.cache import cache
from user import models

def validate_user(func):

    def inner(req, *args, **kwargs):
        if 'HTTP_AUTHORIZATION' not in req.META:
            raise Exception("Token required")
        token = req.META['HTTP_AUTHORIZATION']
        get_user_details(token)
        return func(req, *args, **kwargs)
    return inner

def get_user_details(token):
    user_id = int(cache.get(token))
    user = models.User.objects.filter(id=user_id)
    if user:
        return user[0]
    else:
        raise Exception("Invalid User")