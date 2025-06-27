from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LaminateViewSet, UnderlayViewSet, SkirtingBoardViewSet

router = DefaultRouter()
router.register(r'laminates', LaminateViewSet)
router.register(r'underlays', UnderlayViewSet)
router.register(r'skirting-boards', SkirtingBoardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]