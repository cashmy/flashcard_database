from django.urls import path
from . import views

urlpatterns = [
    path('fcCollections/', views.FcCollectionList.as_view()),
]