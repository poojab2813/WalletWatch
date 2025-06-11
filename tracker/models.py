from django.db import models
from django.contrib.auth.models import User

class Transactions(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense','Expense'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    category = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.transaction_type} - {self.amount}"
