from django.shortcuts import render, redirect
# from django.forms import modelform_factory
from django.contrib.auth.models import User
from .models import Transactions
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
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()            
            return redirect('index')
    else:
        form = TransactionForm()
    context = {
        'form': form
    }           
    return render(request, 'trackerapp/add_expense.html', context)


    



            



