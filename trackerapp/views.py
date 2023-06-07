from django.shortcuts import render
from django.http import HttpResponse
from .models import Transactions


# Create your views here.

def index(request):
    transactions = Transactions.objects.all()
    context = {
        'transactions': transactions
    }
    return render(request, 'trackerapp/index.html', context)


def next(request):
    return HttpResponse("Hello, world. You're here")
