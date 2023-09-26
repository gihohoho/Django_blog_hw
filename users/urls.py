from users import views
from django.urls import path


urlpatterns = [
    path('signup/', views.UserView.as_view(), name='user_view'),
    path('api/token/', views.CustomTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('follow/<int:user_id>/', views.FollowView.as_view(), name='follow_view'),
    path('<int:user_id>/', views.ProfileView.as_view(), name='profile_view'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('myarticle/<int:user_id>/',
         views.MyArticleView.as_view(), name='myarticle_view'),
    path('mycomment/<int:user_id>/',
         views.MyCommentView.as_view(), name='mycomment_view'),
]
