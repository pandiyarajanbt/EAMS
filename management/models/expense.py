from django.db import models
from .project import Project
from django.contrib.auth.models import User


class ExpenseReport(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE,
        related_name='expense_reports'
    )
    requester = models.ForeignKey(
        User, on_delete=models.PROTECT,
        related_name='expense_reports'
    )
    title = models.CharField(max_length=255)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.requester.username})"


class ExpenseReportApproval(models.Model):
    report = models.ForeignKey(
        ExpenseReport, on_delete=models.CASCADE,
        related_name='approvals'
    )
    approver = models.ForeignKey(
        User, on_delete=models.PROTECT,
        related_name='approvals'
    )
    approved = models.BooleanField(default=False)
    comments = models.TextField(blank=True)
    action_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        status = 'Approved' if self.approved else 'Pending'
        return f"{self.report.title} - {self.approver.username}: {status}"


class ExpenseReportProcess(models.Model):
    report = models.OneToOneField(
        ExpenseReport, on_delete=models.CASCADE,
        related_name='process'
    )
    current_stage = models.CharField(
        max_length=100,
        choices=[
            ('draft', 'Draft'),
            ('submitted', 'Submitted'),
            ('in_review', 'In Review'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected'),
        ],
        default='draft'
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.report.title} - {self.get_current_stage_display()}"
