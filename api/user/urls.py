from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views.auth import AuthView
from .views.account import AccountViewSet


router = DefaultRouter()
router.register(r'account', AccountViewSet) 

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('auth/', AuthView.as_view(), name='auth'),

    # Accounts URLs
    path('', include(router.urls)),
]
