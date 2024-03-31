from rest_framework.routers import DefaultRouter
from app import views  

router = DefaultRouter()
router.register('tasks', views.TaskViewSet)  

urlpatterns = router.urls
