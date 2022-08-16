from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_student, name='add_student'),
    path('find/', views.view_student, name='view_student'),
    path('all/', views.view_students, name='view_students'),
    path('update/<int:pk>/', views.update_student, name='update_student'),
    path('student/<int:pk>/delete/', views.delete_student, name='delete_student'),
]
