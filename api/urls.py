from django.urls import path
from api import views

urlpatterns = [
    path('post/', views.ProfileView.as_view(), name='post'),
    path('getdata/', views.ProfileView.as_view(), name='getdata'),
    path('getdata/<int:pk>/', views.ProfileView.as_view(), name='getdata'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('registergetdata/', views.RegisterView.as_view(), name='registergetdata'),
    path('registergetdata/<int:pk>/', views.RegisterView.as_view(), name='registergetdata'),
    path('update/<int:pk>/', views.ProfileView.as_view(), name='update'),
    # path('listget/', views.ListUsers.as_view(), name='listget'),
    path('shakiget/', views.RobotList.as_view(), name='shakiget'),
]