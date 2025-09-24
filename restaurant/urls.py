from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views 

urlpatterns = [
    path('home', views.home, name='home'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]