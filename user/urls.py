from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user'

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='./login.html'), name='login'),
    path('popuplogin/', views.popuplogin, name='popuplogin'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]
