from django.urls import path
from . import views

urlpatterns = [
    path('', views.FcCollectionList.as_view()),
    path('<int:pk>', views.FcCollectionDetail.as_view()),
]