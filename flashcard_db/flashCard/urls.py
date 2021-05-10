from django.urls import path
from . import views

urlpatterns = [
    path('', views.FlashCardList.as_view()),
    path('<int:pk>', views.FlashCardDetail.as_view()),
    path('collection/<int:collection_id>', views.FlashCardCollection.as_view()),
]
