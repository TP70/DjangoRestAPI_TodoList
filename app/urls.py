from django.urls import path, include
from rest_framework import routers
from app.views import TodoListViewSet

router = routers.DefaultRouter()
router.register(r'', TodoListViewSet)

urlpatterns = router.urls
