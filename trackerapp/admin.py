from django.contrib import admin
from .models import AccountCategory, ExpenseCategory, Transactions


admin.site.register(AccountCategory)
admin.site.register(ExpenseCategory)
admin.site.register(Transactions)
