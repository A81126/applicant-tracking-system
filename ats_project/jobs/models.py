from django.db import models

# Create your models here.

from django.db import models


class Job(models.Model):

    JOB_TYPE_CHOICES = (

        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('internship', 'Internship'),

    )

    LOCATION_TYPE_CHOICES = (

        ('remote', 'Remote'),
        ('onsite', 'On Site'),
        ('hybrid', 'Hybrid'),

    )

    STATUS_CHOICES = (

        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('live', 'Live'),
        ('closed', 'Closed'),

    )

    title = models.CharField(max_length=255)

    description = models.TextField()

    pay_start = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    pay_end = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    location = models.CharField(max_length=255)

    job_type = models.CharField(
        max_length=20,
        choices=JOB_TYPE_CHOICES
    )

    location_type = models.CharField(
        max_length=20,
        choices=LOCATION_TYPE_CHOICES
    )

    cover_letter_required = models.BooleanField(
        default=False
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )

    slug = models.SlugField(
        unique=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title




COVER_LETTER_CHOICES = (
    (True, "Yes"),
    (False, "No"),
)

cover_letter_required = models.BooleanField(
    default=True
)
