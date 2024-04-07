from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('update/<int:pk>/', views.user_update, name='user_update'),
    path('delete/<int:pk>/', views.user_delete, name='user_delete'),
]
