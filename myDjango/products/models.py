from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    # date_added = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    
    
    def __str__(self):
        return self.name