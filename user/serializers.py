from rest_framework import serializers
from .models import *
from djoser.serializers import UserSerializer


class UserSerializer(UserSerializer):

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + \
            (User.USERNAME_FIELD, 'last_login', 'last_activity')
        read_only_fields = (User.USERNAME_FIELD,)
