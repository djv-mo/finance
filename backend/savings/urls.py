from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .viewsets import SavingGoalViewSet

router = DefaultRouter()
router.register(r'saving-goals', SavingGoalViewSet, basename='saving-goals')

urlpatterns = [
    path('', include(router.urls)),
]
