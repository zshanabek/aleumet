from django.utils.timezone import now
from rest_framework.authtoken.models import Token
from re import sub
from .models import User


class SetLastVisitMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        header_token = request.META.get('HTTP_AUTHORIZATION', None)
        if header_token is not None:
            try:
                token = sub('Token ', '', header_token)
                token_obj = Token.objects.get(key=token)
                request.user = token_obj.user
                user = User.objects.get(id=request.user.id)
                user.last_activity = now()
                user.save()
            except Token.DoesNotExist:
                pass

        return self.get_response(request)
