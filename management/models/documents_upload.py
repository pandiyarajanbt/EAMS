from typing import Any, ByteString
from django.db import models

#models
from .profile import Profile
class Documents(models.Model):
    profiles  = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='profiles')
    payslip = models.FileField(upload_to='media/Documents/payslip/', null=True, blank=True)
    exp_documents = models.FileField(upload_to='media/Documents/exp_documents/', null=True, blank=True)
    offer_letter = models.FileField(upload_to='media/Documents/offer_letter/', null=True, blank=True)
    pan_card = models.FileField(upload_to='media/Documents/pan_card/', null=True, blank=True)
    aadhar_card = models.FileField(upload_to='media/Documents/aadhar_card/', null=False, blank=False)
    mark_sheet = models.FileField(upload_to='media/Documents/mark_sheet/', null=False, blank=False)
    documents_title = models.CharField(max_length=55, null=False, blank=False)
    other_documents = models.FileField(upload_to='media/Documents/other_documents/', null=False, blank=False)

    def __init__(self, *args: ByteString, **kwargs: ByteString) -> None:
        return self.profiles
