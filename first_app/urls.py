from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student_create', views.create_student, name='student create'),
    path('detail/<int:id>/', views.detail, name='detail')
]