from django.urls import path
from api import views

urlpatterns = [
    path('post/', views.ProfileView.as_view(), name='post'),
    path('getdata/', views.ProfileView.as_view(), name='getdata'),
    path('register/', views.ProfileView.as_view(), name='register'),
    path('update/', views.ProfileView.as_view(), name='update'),
]