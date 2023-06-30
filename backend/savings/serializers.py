from rest_framework import serializers

from .models import SavingGoal


class SavingGoalSerializer(serializers.ModelSerializer):
    monthly_deposit = serializers.ReadOnlyField()
    class Meta:
        model = SavingGoal
        fields = ['id', 'amount', 'date', 'monthly_deposit']
