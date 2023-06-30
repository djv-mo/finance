from django.contrib import admin

from .models import SavingGoal


@admin.register(SavingGoal)
class SavingGoalsAdmin(admin.ModelAdmin):
    readonly_fields = ["monthly_deposit",]