from django.db import models
from django.contrib.auth.models import User
from issues.models import Issues, IssueStatus

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserIssues(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    issue = models.ForeignKey(Issues, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(IssueStatus, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




