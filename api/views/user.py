from rest_framework import viewsets
from api.serializers import UserSerializer, UserRegisterSerializer, UserLoginSerializer
from core.models.user import User
from rest_framework import generics,views
from rest_framework.response import Response
from django.contrib.auth import login, logout
from django.shortcuts import redirect

class UserRegisterView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

class UserLoginView(views.APIView):
    def post(self,request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

class Logout(views.APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        logout(request)
        return redirect("login_view")

# class UserViewSet(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
