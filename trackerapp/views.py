from django.shortcuts import render, redirect, get_object_or_404
# from django.forms import modelform_factory
from django.contrib.auth.models import User
from .models import Transactions, ExpenseCategory, AccountCategory
from .forms import TransactionForm


def index(request):
    transactions = Transactions.objects.filter(user=request.user)
    balance = 0   
    for transaction in transactions:
        if transaction.transaction_type == 'Income':
            balance += transaction.amount
        else:
            balance -= transaction.amount
        
    context = {
        'transactions': transactions,
        'balance': balance        
    }
    return render(request, 'trackerapp/index.html', context)


def add_expense(request):
    # form = TransactionForm(initial={'transaction_type': 'Expense'})
    
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            # get the user account category
            user = request.user            
            account_category = AccountCategory.objects.get(user=user)

            # get the expense category instance
            expense_category_option = form.cleaned_data['expense_category']
            expense_category = get_object_or_404(
                ExpenseCategory, 
                category_name = expense_category_option, 
                user = user
            )

            # create transaction with the expense category
            transaction = form.save(commit=False)
            transaction.user = user
            transaction.account_category = account_category
            transaction.expense_category = expense_category
            form.save()       
            return redirect('index')
    else:
        form = TransactionForm()
    context = {
        'form': form
    }           
    return render(request, 'trackerapp/add_expense.html', context)


def add_income(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            # get the user account category
            user = request.user            
            account_category = AccountCategory.objects.get(user=user)

            # get the expense category instance
            expense_category_option = form.cleaned_data['expense_category']
            expense_category = get_object_or_404(
                ExpenseCategory, 
                category_name = expense_category_option, 
                user = user
            )

            # create transaction with the expense category
            transaction = form.save(commit=False)
            transaction.user = user
            transaction.account_category = account_category
            transaction.expense_category = expense_category
            form.save()       
            return redirect('index')
    else:
        form = TransactionForm()
    context = {
        'form': form
    }           
    return render(request, 'trackerapp/add_income.html', context)



    




            



