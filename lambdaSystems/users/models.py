from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    """Model base for Admin and Salesman."""
    name = models.CharField(max_length=120)
    identification_document = models.CharField(max_length=10, default="none")
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class Admin(Profile):
    """Model for admin user."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admin_id = models.AutoField(
        primary_key=True, unique=True, auto_created=True)


class Salesman(Profile):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    count_sells = models.IntegerField(default=0)
    earnings = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    seller_id = models.AutoField(
        auto_created=True, primary_key=True, unique=True)
    picture = models.ImageField(
        upload_to="users/pictures",
        blank=True,
        null=True
    )
