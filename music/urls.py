from django.urls import path
from . import views
from django.views.generic.base import TemplateView

app_name = 'music'

urlpatterns = [
    path('', TemplateView.as_view(template_name='music/music_home.html'), name='music_home'),
    path('login/', views.login, name='login')
]