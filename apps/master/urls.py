from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='accounts_index'),
    path('accounts/login', views.LoginView.as_view(), name='login'),
    path('accounts/signup', views.SignupView.as_view(), name='signup'),
    path('accounts/logout', views.logout_view, name='logout')
]