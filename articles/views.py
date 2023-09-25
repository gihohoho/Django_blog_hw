from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response

from articles.models import Article


# 첫화면
class ArticleView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        pass


# 모아보기(feed)
class FeedView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        pass


# 게시글 상세보기
class ArticleDetailView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        pass
