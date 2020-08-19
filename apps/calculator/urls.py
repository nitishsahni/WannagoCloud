from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='pricing_index'),
    path('baas', login_required(views.BaaS_View.as_view(), login_url='login'), name='pricing_baas'),
    path('iaas', login_required(views.IaaS_View.as_view(), login_url='login'), name='pricing_iaas')

]