from django.db import models


class Issues(models.Model):
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=100)


class IssueStatus(models.Model):
    PENDING = "pending"
    CONSTRUCTION = "construction"
    INSPECTION = "inspection"
    COMPLETED = "completed"
    STATUS_CHOICES = ((PENDING, "Pending"),
                      (CONSTRUCTION, "Construction"),
                      (INSPECTION, "inspection"),
                      (COMPLETED, "completed"))
    name = models.CharField(choices=STATUS_CHOICES, max_length=100)

# Create your models here.
