from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from datetime import date


#---------- ACCOUNT CATEGORY (e.g. cash, savings, cards)
class AccountCategory(models.Model):    

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=200, unique=True, default='Cash')
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.account_name  

       

#---------- EXPENSES CATEGORIS
class ExpenseCategory(models.Model):    

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.category_name
        
    
    # list of transactions by category
    def show_category_expenses(self):
        expenses_list = Transactions.objects.filter(expense_category=self)
        return expenses_list


#---------- TRANSACTIONS
class Transactions(models.Model):
    TRANSACTION_TYPE_CHOICE = (('Expense', 'Expense'), ('Income', 'Income'))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_category = models.ForeignKey(AccountCategory, on_delete=models.CASCADE, default=None, blank=True, null=True)
    expense_category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE, default=None, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPE_CHOICE)
    transaction_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True)   
    
    def __str__(self):
        if self.transaction_type == 'Income':
            income_icon = '<i class="fa-solid fa-sack-dollar fa-xl"></i>'
            return mark_safe(f'${self.amount} - {income_icon}')
        else:
            return f'${self.amount} - {self.expense_category} - {self.transaction_type}'
    

  
    
    

    

   

   
