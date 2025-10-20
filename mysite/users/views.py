from django.shortcuts import render

# Create your views here.
#users/views.py
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Получение access и refresh токенов.
    Refresh токен сохраняется в HttpOnly cookie.
    """
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        refresh = RefreshToken.for_user(user)
        access = str(refresh.access_token)

        response = Response({"access": access}, status=status.HTTP_200_OK)
        response.set_cookie(
            key="refresh_token",
            value=str(refresh),
            httponly=True,
            secure=False,  # True на HTTPS
            samesite="Lax",
            max_age=7*24*60*60  # 7 дней
        )
        return response


class CustomTokenRefreshView(APIView):
    """
    Обновление access токена с помощью refresh токена из cookie.
    """
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get("refresh_token")
        if not refresh_token:
            return Response({"detail": "Нет refresh токена"}, status=401)
        try:
            refresh = RefreshToken(refresh_token)
            access = str(refresh.access_token)
            return Response({"access": access})
        except Exception:
            return Response({"detail": "Неверный или просроченный refresh токен"}, status=401)

