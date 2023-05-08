from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import SigninForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('signin/', auth_views.LoginView.as_view(template_name='core/signin.html', authentication_form=SigninForm), name='signin'),
    path('logout/', views.view_logout, name='logout'),
]
