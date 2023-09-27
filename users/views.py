from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from users.models import User
from users.serializers import DeleteAccountSerializer, MyArticleSerializer, MyCommentSerializer, UserSerializer, MyTokenObtainPairSerializer, UserProfileSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib.auth import logout as auth_logout


# 회원가입
class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "가입완료"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": f'$(serializer.errors)'}, status=status.HTTP_400_BAD_REQUEST)


# 로그인
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# 로그아웃
class Logout(APIView):
    def post(self, request):
        auth_logout(request)
        return Response({"message": "로그아웃 완료"}, status=status.HTTP_200_OK)


# 팔로우
class FollowView(APIView):
    def post(self, request, user_id):
        you = get_object_or_404(User, id=user_id)
        me = request.user
        if me in you.followers.all():
            you.followers.remove(me)
            return Response("팔로우 취소", status=status.HTTP_200_OK)
        else:
            you.followers.add(me)
            return Response("팔로우 완료", status=status.HTTP_200_OK)


# 프로필
class ProfileView(APIView):
    def get(self, requset, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)


# 게시글 조회
class MyArticleView(APIView):
    def get(self, requset, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = MyArticleSerializer(user)
        return Response(serializer.data)


# 댓글 조회
class MyCommentView(APIView):
    def get(self, requset, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = MyCommentSerializer(user)
        return Response(serializer.data)


# 회원 탈퇴
# generics.DestroyAPIView 안쓰고도 가능한지? / password 받아서 탈퇴 힌트,,,
class DeleteAccountView(generics.DestroyAPIView):
    def delete(self, request, user_id):
        serializer_class = DeleteAccountSerializer
        permission_classes = [permissions.IsAuthenticated]
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return Response("회원탈퇴 완료", status=status.HTTP_200_OK)
