from uuid import uuid4

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class SavingGoalManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

class SavingGoal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='savings')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Total amount'))
    date = models.DateField(verbose_name=_('Date to reach goal'))
    monthly_deposit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Monthly deposite'))
    created_at = models.DateTimeField(auto_now_add=True)
    objects = SavingGoalManager()
    
    class Meta:
        verbose_name = "Saving Goal"
        verbose_name_plural = "Saving Goals"
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.user.username}'s Saving Goal: {self.amount}"
    
    def save(self, *args, **kwargs):
        self.monthly_deposit = self.set_monthly_deposit()
        super().save(*args, **kwargs)
    
    def set_monthly_deposit(self):
        # Calculate the monthly deposit based on the total amount and goal date
        current_date = timezone.localdate()
        months_remaining = (self.date.year - current_date.year) * 12 + (self.date.month - current_date.month)
        if months_remaining == 0:
            months_remaining = 1
        return self.amount / months_remaining


