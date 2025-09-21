from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from . import views 

urlpatterns = [
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]