from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="polls_welcome_page"),
    path("polls_welcome", views.polls_welcome_page2, name="polls_welcome_page2")
]