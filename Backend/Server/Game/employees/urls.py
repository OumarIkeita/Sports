from django.urls import path
from . import views
urlpatterns=[
    path('employees/',views.home, name="employees")
]