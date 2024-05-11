from django.urls import path
from rest_apis.views import CustomTokenGeneration, CustomTokenObtainPairView, Home, LogoutAllView, LogoutView
from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'), #using jwt in built librarry
    path('token/', CustomTokenGeneration.as_view(), name='token_obtain_pair'), #generate token manually
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
    path("home/", Home.as_view(), name="home"),
]