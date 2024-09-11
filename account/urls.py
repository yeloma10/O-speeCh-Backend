from django.urls import path
from .views import *
from rest_framework_simplejwt.views import ( # type: ignore
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/register/', UserCreateView.as_view(), name='user-register'),
    path('api/token/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/<int:id>/', UserProfileView.as_view(), name='user-profile'),
]
