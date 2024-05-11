from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_apis.serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User



class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer


class Home(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        print('received request')
        return Response({'SUCCESS': True, 'message':'Received Request, Response is from Django 5.2 Development Server'},
                         status=status.HTTP_200_OK)
    


# Create a custom for implementation of secure 
class CustomTokenGeneration(APIView):

    def post(self, request):
        print('request.data', request.data)
        user = User.objects.get(email='admin@gmail.com')
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)



class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            print(request.data["refresh_token"])
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            print('token', token)
            # raise Exception()
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutAllView(APIView):
    pass