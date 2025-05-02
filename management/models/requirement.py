from django.db import models
from .project import Project
from .profile import Profile


class Requirement(models.Model):
    requester = models.ForeignKey(
        Profile, on_delete=models.PROTECT,
        related_name='requirements'
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE,
        related_name='requirements'
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Requirement for {self.project.name} by {self.requester.username}"


class RequirementItem(models.Model):
    requirement = models.ForeignKey(
        Requirement, on_delete=models.CASCADE,
        related_name='items'
    )
    purchase_requirement = models.TextField()
    reference_price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.purchase_requirement