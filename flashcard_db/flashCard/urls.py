from django.urls import path
from . import views

urlpatterns = [
    path('flashCard/', views.FlashCardList.as_view()),
]
