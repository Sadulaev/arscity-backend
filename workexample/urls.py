from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkExampleViewSet

router = DefaultRouter()
router.register(r'work-examples', WorkExampleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]