from django.urls import path
from .import views
urlpatterns = [
    path('login/',views.loging.as_view(), name='login')
]
