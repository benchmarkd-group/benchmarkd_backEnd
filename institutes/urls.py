from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.InstituteAPIView.as_view()),
    path('<str:insti_name_val>', views.InstituteDetailAPIView.as_view()),
    path('exams/<str:insti_name_val>', views.InstituteExamAPIView.as_view()),
    path('like/<str:insti_name_val>', views.InstituteLikeAPIView.as_view())

]