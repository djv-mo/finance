from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import SavingGoal
from .permissions import IsOwner
from .serializers import SavingGoalSerializer


class SavingGoalViewSet(viewsets.ModelViewSet):
    serializer_class = SavingGoalSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return SavingGoal.objects.filter(user=user)