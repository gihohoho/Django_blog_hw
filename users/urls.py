from users import views
from django.urls import path


urlpatterns = [
    path('signup/', views.UserView.as_view(), name='user_view'),
    path('api/token/', views.CustomTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
]
