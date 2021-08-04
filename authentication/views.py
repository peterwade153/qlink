from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from authentication.models import User
from authentication.serializers import UserSerializer


class UserView(APIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)

    def post(self, request):
        """
        Creates new users
        params :
            - email
            - password
        """
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            email = data.get("email", None)
            user_exists = User.objects.filter(email=email).exists()
            if user_exists:
                return Response({
                    "detail": 'User already exists, Login',
                    "message": "failed"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            # Create a new user
            serializer.save()
            return Response({
                "detail": "User account created",
                "message": "success"
                },
                status=status.HTTP_201_CREATED
            )
        else:
            return Response({
                "detail": serializer.errors,
                "message": "failed"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
