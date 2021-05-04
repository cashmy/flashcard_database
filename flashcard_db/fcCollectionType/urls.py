from django.urls import path
from . import views

urlpatterns = [
    path('', views.FcCollectionTypeList.as_view()),
    path('<str:pk>', views.FcCollectionTypeDetail.as_view()),
]
