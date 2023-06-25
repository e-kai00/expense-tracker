from django.db import models
from django.contrib.auth.models import User


# ---------- ACCOUNT CATEGORY (e.g. cash, savings, cards)
class AccountCategory(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    account_name = models.CharField(
        max_length=200,
        unique=True,
        default='Cash')
    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.0)

    def __str__(self):
        return self.account_name


# ---------- EXPENSES CATEGORIS
class ExpenseCategory(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    category_name = models.CharField(
        max_length=200)

    class Meta:
        ordering = ['category_name']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'category_name'],
                name='unique_category-per_user'
            )
        ]

    def __str__(self):
        return self.category_name


# ---------- TRANSACTIONS
class Transactions(models.Model):
    TRANSACTION_TYPE_CHOICE = (('Expense', 'Expense'), ('Income', 'Income'))

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    expense_category = models.ForeignKey(
        ExpenseCategory,
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2)
    transaction_type = models.CharField(
        max_length=7,
        choices=TRANSACTION_TYPE_CHOICE)
    transaction_date = models.DateField(
        auto_now_add=True)
    notes = models.TextField(
        blank=True)

    def __str__(self):
        if self.transaction_type == 'Income':
            return f'{self.transaction_type}  ${self.amount}'
        else:
            return f'{self.expense_category}  ${self.amount}'
