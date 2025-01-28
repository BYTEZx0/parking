from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('login/', views.user_login, name='login'),
    path('registration/security', views.security_page, name='security'),
    path('api/parking-spots/', views.get_parking_spots, name='parking-spots'),
]