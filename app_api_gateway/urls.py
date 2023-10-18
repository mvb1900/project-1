from django.urls import path, include
from rest_framework import routers

from app_todolist.views import TaskAPIView

router = routers.SimpleRouter()
router.register('task', TaskAPIView, 'task')

urlpatterns = [
    path('', include(router.urls)),
]
