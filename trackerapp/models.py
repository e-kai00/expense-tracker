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
    

class ExpenseCategory(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.category_name
    

    def get_total_expenses(self):
        total = 0
        expense = Transactions.objects.filter(categoty_name=self)
        for expense in expenses:
            total += expense.amount
        return total


    def show_category_expenses(self):
        expenses_list = Transactions.objects.filter(category=self)
        return expenses_list


class Transactions(models.Model):
    TRANSACTION_TYPE_CHOICE = (('Expense', 'Expense'), ('Income', 'Income'))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_category = models.ForeignKey(AccountCategory, on_delete=models.CASCADE)
    expense_category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=7, unique=True, choices=TRANSACTION_TYPE_CHOICE)
    transaction_date = models.DateField()
    notes = models.TextField()

   
