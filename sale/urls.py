from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TileViewSet, LaminateViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'tiles', TileViewSet)
router.register(r'laminates', LaminateViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]