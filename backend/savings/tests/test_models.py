from datetime import datetime
from decimal import ROUND_HALF_UP, Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import SavingGoal

# tests/test_models.py


class SavingGoalModelTests(TestCase):
    def test_saving_goal_creation(self):
        user = get_user_model().objects.create(username='testuser')
        saving_goal = SavingGoal.objects.create(
            user=user,
            amount=1000,
            date=datetime.strptime('2023-12-31', '%Y-%m-%d').date(),
        )
        expected_monthly_deposit = Decimal(1000) / 5
        expected_monthly_deposit = expected_monthly_deposit.quantize(
            Decimal('0.00'), rounding=ROUND_HALF_UP
        )
        self.assertEqual(saving_goal.monthly_deposit, expected_monthly_deposit)


