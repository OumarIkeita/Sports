from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.students, name='students'),
    path('student/<int:id>/', views.singleStudent, name='student'),
    path('courses/', views.courses, name="courses")
]
