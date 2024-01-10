from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed

from django.contrib.auth.models import User
from services.jwt_service import JwtService

class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = self.get_token(request)
        jwt_service = JwtService()
        if token is None:
            raise AuthenticationFailed
        try:
            payload = jwt_service.decode_token(token)
            user_id = payload.get('user_id')
            user = User.objects.get(id=user_id)
            return (user, None)
        except Exception:
            raise AuthenticationFailed
            
    def get_token(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if auth_header is None:
            return None
        _, token = auth_header.split()
        return token