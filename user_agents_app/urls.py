from django.urls import path
from . import views

urlpatterns = [
    path('user-agent/', views.index, name='index'),
    path('info_device/', views.get_agent, name='info_device'),
    path('user-agent/info', views.info_user_agent, name='info_user_agent'),
]