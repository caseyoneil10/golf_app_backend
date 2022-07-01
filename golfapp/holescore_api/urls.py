from django.urls import path
from . import views

urlpatterns = [
    path('api/holescore', views.HolescoreList.as_view(), name='holescore_list'),
    path('api/holescore/<int:pk>', views.HolescoreDetail.as_view(), name='holescore_detail'),
]
