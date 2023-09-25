from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response

from articles.models import Article
from articles.serializers import ArticleCreateSerializer, ArticleListSerializer



# 첫화면
class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArticleCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
