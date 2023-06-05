from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User


class AccountCategory(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=200, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.account_name
    

    def update_balance(self, amount, operation):
        if operation == 'add':
            self.balance += amount
        else:
            self.balance -= amount
        
        self.save()


    def is_sufficient_balance(self, amount):
        return self.balance >= amount
    

    @classmethod
    def calculate_total_balance(cls, user):
        total_balance = cls.objects.filter(user=user).aaggregate(total_balance=Sum('balance'))
        return total_balance['total_balance']


