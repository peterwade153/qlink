import jwt
from django.conf import settings
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed

from authentication.models import User, TokenBlacklist


class JSONWebTokenAuthentication(authentication.BaseAuthentication):
    """
    Custom JWT authentication for the API
    """
    def authenticate(self, request):
        token = self._get_token(request)

        # Check for blacklisted token
        blacklist = TokenBlacklist.objects.filter(token=token).first()
        if blacklist:
            raise AuthenticationFailed('Invalid token, Please login')
        return self._get_user_details(token)

    @staticmethod
    def _get_token(request):
        """
        Get access token from the headers
        """
        access_token = request.headers.get('Authorization')
        if not access_token:
            return None
        token =  access_token.split(' ')[1]
        return token

    @staticmethod
    def _get_user_details(token):
        """
        Decode the token to get user details
        """
        try:
            payload = jwt.decode(
                token, 
                settings.SECRET_KEY, 
                algorithms=['HS256']
            )
            user = User.objects.get(email=payload['email'])
        except (jwt.DecodeError, User.DoesNotExist):
            raise AuthenticationFailed('Invalid token')
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except:
            raise AuthenticationFailed('Invalid token, Please Login')

        if not user.is_active:
            raise AuthenticationFailed('User inactive')
        return (user, token)
