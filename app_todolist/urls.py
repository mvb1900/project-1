from .views import todo_list_view
from django.urls import path


urlpatterns = [
    path("", todo_list_view, name="todo_list_view")
]
