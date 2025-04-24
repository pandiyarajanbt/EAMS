from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=255)
    business_unit = models.ForeignKey(
        'BusinessUnit', on_delete=models.PROTECT,
        related_name='projects'
    )
    owner = models.ForeignKey(
        User, on_delete=models.PROTECT,
        related_name='owned_projects'
    )
    start_date = models.DateField()
    expected_budget = models.DecimalField(max_digits=12, decimal_places=2)
    expected_completion = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class BusinessUnit(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name