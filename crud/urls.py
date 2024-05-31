from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:my_id>/', views.update_page, name='update_page')
]