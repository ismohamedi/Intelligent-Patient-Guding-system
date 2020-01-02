from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='login'),
    path('patient_information', views.patient_info, name='patient_info'),
    path('chat', views.chatbot, name='chat')
]