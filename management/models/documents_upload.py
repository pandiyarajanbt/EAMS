from typing import Any, ByteString
from django.db import models

#models
from .profile import Profile


class Documents(models.Model):
    profiles  = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='profiles')
    Payslip = models.FileField(upload_to='media/Documents/', null=True, blank=True)
    exp_documents = models.FileField(upload_to='media/Documents/', null=True, blank=True)
    offer_letter = models.FileField(upload_to='media/Documents/', null=True, blank=True)
    pan_card = models.FileField(upload_to='media/Documents/', null=True, blank=True)
    Aadhar_card = models.FileField(upload_to='media/Documents/', null=True, blank=True)

    def __init__(self, *args: ByteString, **kwargs: ByteString) -> None:
        return self.profiles
