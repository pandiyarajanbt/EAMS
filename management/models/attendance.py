from django.db import models
from .profile import Profile

class Attendance(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE,
        related_name='attendances'
    )
    date = models.DateField()
    check_in = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)
    is_present = models.BooleanField(default=False)

    class Meta:
        unique_together = ('profile', 'date')

    def __str__(self):
        status = 'Present' if self.is_present else 'Absent'
        return f"{self.profile.name} on {self.date}: {status}"


class FaceRecognitionRecord(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE,
        related_name='face_records'
    )
    image = models.ImageField(upload_to='face_recognition/')
    recognized_at = models.DateTimeField(auto_now_add=True)
    confidence_score = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Face record for {self.profile.name} at {self.recognized_at}"
