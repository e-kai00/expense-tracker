from django.db import models
from django.contrib.auth.models import User
from datetime import date


#---------- ACCOUNT CATEGORY (e.g. cash, savings, cards)
class AccountCategory(models.Model):    

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=200, unique=True, default='Cash')
    balance = models.DecimalField(max_digits=10, decimal_places=2)  


    def __str__(self):
        return self.account_name
    

    def total_balance(self):
        total_balance = Transactions.objects.filter(user=self.user)
        return total_balance.get_balance()
    

    def update_balance(self, amount, operation):
        current_balance = self.total_balance()
        if operation == 'add':
            current_balance += amount
        else:
            current_balance -= amount        
        self.balance = current_balance
        self.save()


    def is_sufficient_balance(self, amount):
        return self.total_balance() >= amount
    

    def trasfer_funds(self, target_account, amount):
        if self.is_sufficient_balance(amount):
            self.update_balance(amount, 'subtract')
            target_account.update_balance(amount, 'add')
            return True
        else:
            False
    
    
#---------- EXPENSES CATEGORIS
class ExpenseCategory(models.Model):
    CATEGORIES = (
        ('Bills', 'Bills'),
        ('Clothes', 'Clothes'),
        ('Entertainment', 'Entertainment'),
        ('Food', 'Food'),
        ('Gifts', 'Gifts'),
        ('Health', 'Health'),        
        ('Pets', 'Pets'),
        ('Transport', 'Transport')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=200, unique=True, choices=CATEGORIES)

    def __str__(self):
        return self.category_name
    
    # total expenses by category
    def get_total_expenses(self):
        total = 0
        expenses = Transactions.objects.filter(expense_categoty=self)
        for expense in expenses:
            total += expense.amount
        return total

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
        return f'{self.expense_category} - {self.transaction_type} - {self.amount}'       
    

    def transactions_list(self):
        return Transactions.objects.filter(user=self.user)
    

    def get_total_expenses(self):
        total = 0
        expenses_list = Transactions.objects.filter(user=self.user, transaction_type='Expense')
        for expense in expenses_list:
            total += expense.amount
        return total
    

    def get_total_income(self):
        total = 0
        income_list = Transactions.objects.filter(user=self.user, transaction_type='Income')
        for income in income_list:
            total += income.amount
        return total
    

    def get_balance(self):    # to remove
        balance = 0
        transactions = Transactions.objects.filter(user=self.user)
        for transaction in transactions:
            if transaction.transaction_type == 'Income':
                balance += transaction.amount
            else:
                balance -= transaction.amount
        return balance
    

    def filter_by_month(self, month):
        current_year = date.today().year
        return Transactions.objects.filter(
            user=self.user, 
            transaction_date__month=month, 
            transaction_date__year=current_year
        )

    

   

   
