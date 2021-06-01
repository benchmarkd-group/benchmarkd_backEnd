from django.conf.urls import url
from django.urls.conf import path

from . import views

urlpatterns = [
    path('', views.CourseView.as_view()),
    path('<str:course_id_val>', views.CourseDetailAPIView.as_view()),

]