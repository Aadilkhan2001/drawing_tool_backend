import jwt

from datetime import datetime, timedelta
from django.conf import settings

class JwtService:
    @classmethod
    def generate_token(cls, user_id):
        """
        Generate a JWT token for the given user ID.
        """

        payload = {
            'user_id': user_id,
            'exp': datetime.utcnow() + timedelta(seconds=settings.JWT_EXPIRATION_DELTA),
            'iat': datetime.utcnow(),
        }
        return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

    @classmethod
    def decode_token(cls, token):
        """
        Decode a JWT token and retrieve the payload.
        """
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            # Token has expired
            return {'error': 'Token has expired.'}
        except jwt.InvalidTokenError:
            # Invalid token
            return {'error': 'Invalid token.'}
