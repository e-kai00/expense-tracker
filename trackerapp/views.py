from django.shortcuts import render
from django.http import HttpResponse
from .models import Transactions
from django.contrib.auth.models import User


# Create your views here.

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



