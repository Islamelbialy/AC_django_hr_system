from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('signUp/',SignUpView.as_view(),name='signUp'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('changePassword/',PasswordChange.as_view(),name='changePassword'),
]