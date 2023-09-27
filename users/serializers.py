from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from articles.serializers import ArticleListSerializer, CommentSerializer


class UserProfileSerializer(TokenObtainPairSerializer):
    followers = serializers.StringRelatedField(many=True)
    followings = serializers.StringRelatedField(many=True)
    like_articles = ArticleListSerializer(many=True)

    class Meta:
        model = User
        fields = ("id", "email", "followers", "followings", "like_articles", )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user

    def update(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email

        return token


class MyArticleSerializer(TokenObtainPairSerializer):
    article_set = ArticleListSerializer(many=True)

    class Meta:
        model = User
        fields = ("like_articles",)


class MyCommentSerializer(TokenObtainPairSerializer):
    comment_set = CommentSerializer(many=True)

    class Meta:
        model = User
        fields = ("comment_set",)


class DeleteAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
