from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginListCreate.as_view()),
]
