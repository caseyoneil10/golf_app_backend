from django.urls import path
from . import views

urlpatterns = [
    path('api/courses', views.CourseList.as_view(), name='course_list'),
    path('api/courses/<int:pk>', views.CourseDetail.as_view(), name='course_detail'),
]
