from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from users.models import User


# 회원가입
class UserView(APIView):
    def post(self, request):
        pass
