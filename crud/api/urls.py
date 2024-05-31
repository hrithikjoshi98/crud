from django.urls import path, include
from crud.api import views
from rest_framework.routers import DefaultRouter
from .views import register, login, protected, get_csrf_token
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
# router.register('crud', views.UserViewSet, basename='user')
router.register('product', views.ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework')),

    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('protected/', protected, name='protected'),
    path('get-csrf-token/', get_csrf_token),
]
