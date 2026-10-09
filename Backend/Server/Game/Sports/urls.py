from django.urls import path
from .import views
urlpatterns = [
    path('clubs/',views.Clubs, name='clubs'),
    path('club/<int:id>/',views.singleClub, name='club'),
    path('clubIs/<str:query>/',views.singleClubs, name='clubIs'),
]
