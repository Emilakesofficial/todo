from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.TodoView.as_view()),
    path('todos/<str:id>/', views.TodoDetailView.as_view())
]