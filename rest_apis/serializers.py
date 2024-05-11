from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import json


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['last_login'] = user.last_login.isoformat() if user.last_login else None
        token['account_created'] = user.date_joined.isoformat()
        return token