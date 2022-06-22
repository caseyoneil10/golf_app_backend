from django.urls import path
from . import views

urlpatterns = [
    path('api/scores', views.ScoreList.as_view(), name='score_list'),
    path('api/scores/<int:pk>', views.ScoreDetail.as_view(), name='score_detail'), 
]
