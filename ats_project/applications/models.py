from django.db import models

# Create your models here.

from django.db import models
from jobs.models import Job


# class Application(models.Model):

#     job = models.ForeignKey(
#         Job,
#         on_delete=models.CASCADE,
#         related_name="applications"
#     )

#     name = models.CharField(max_length=255)

#     email = models.EmailField()

#     phone = models.CharField(max_length=20)

#     resume = models.FileField(
#         upload_to="resumes/"
#     )

#     cover_letter = models.TextField(
#         blank=True,
#         null=True
#     )

#     created_at = models.DateTimeField(
#         auto_now_add=True
#     )

#     def __str__(self):
#         return self.name

class Application(models.Model):

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=255)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    resume = models.FileField(
        upload_to="resumes/"
    )

    cover_letter = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )