from django.urls import path
from . import views

urlpatterns = [
    path('api/holeScore', views.HoleScoreList.as_view(), name='holeScore_list'),
    path('api/holeScore/<int:pk>', views.HoleScoreDetail.as_view(), name='holeScore_detail'),
]
