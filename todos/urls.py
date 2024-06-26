from django.urls import path
from todos.views import TodoAPIView, TodoDetailAPIView

urlpatterns = [
    path('', TodoAPIView.as_view(), name='todos'),
    path('<int:id>', TodoDetailAPIView.as_view(), name='todo')
]