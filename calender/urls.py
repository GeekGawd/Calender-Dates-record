from django.urls import path
from . import views

urlpatterns = [
    path('calender/', views.Relapse.as_view()),
]
