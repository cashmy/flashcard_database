from django.urls import path
from . import views

urlpatterns = [
    path('fcCollectionType/', views.FcCollectionTypeList.as_view()),
]
