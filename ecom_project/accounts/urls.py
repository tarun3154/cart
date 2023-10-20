from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.Userlogout, name='logout'),
    path('registration/', views.registration, name='register'),

]
