from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    weight = models.IntegerField()
    created_at =models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
