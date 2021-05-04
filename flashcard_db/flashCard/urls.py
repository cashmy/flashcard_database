from django.urls import path
from . import views

urlpatterns = [
    path('', views.FlashCardList.as_view()),
    path('<int:pk>', views.FlashCardDetail.as_view())
]
