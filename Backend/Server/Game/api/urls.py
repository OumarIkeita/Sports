from django.urls import path
from . import views
urlpatterns= [
    path('students/', views.students , name ="students"),
    path('student/<int:pk>/', views.student_detail , name ="student"),
    path('studentUpdate/<int:pk>/', views.student_update , name ="studentupdate"),
    path("studentDelete/<int:pk>/", views.student_delete, name="studentdelete"),
    path('employee/', views.EmployeeView.as_view(), name='employee'),
    path('employee/<int:pk>/', views.EmployeeDetail.as_view(), name='employee'),
    path('social/', views.Socials.as_view(), name='social'),
    path('societe/<int:pk>/', views.Society.as_view(), name='societe'),
]