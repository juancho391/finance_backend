from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer, UserResponse, UserRLoginSerializer
from .models import User
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import gettext_lazy as _

# Create your views here.


class UserRegisterView(APIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            return Response(
                {
                    "message": _("User created successfully"),
                    "user": UserResponse(user).data,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    serializer = UserRLoginSerializer

    def post(self, request):
        user = get_object_or_404(User, username=request.data["username"])
        if user.check_password(request.data["password"]):
            return Response(
                {
                    "message": _("User logged in successfully"),
                    "user": UserResponse(user).data,
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {"message": _("Invalid credentials")}, status=status.HTTP_401_UNAUTHORIZED
        )
