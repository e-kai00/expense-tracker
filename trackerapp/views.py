from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Transactions, ExpenseCategory, AccountCategory
from .forms import TransactionForm, TransactionIncomeForm, AddCategoryForm, EditCategoryForm
import datetime


def index(request):
    # get the current month and year
    now = datetime.datetime.now()
    year = now.year
    month = now.month

    if request.user.is_authenticated: 
        transactions = Transactions.objects.filter(
            user=request.user,
            transaction_date__year=year,
            transaction_date__month=month
    )

        balance = 0   
        for transaction in transactions:
            if transaction.transaction_type == 'Income':
                balance += transaction.amount
            else:
                balance -= transaction.amount

    else:
        transactions = None
        balance = None

        
    context = {
        'transactions': transactions,
        'balance': balance        
    }
    return render(request, 'trackerapp/index.html', context)


def add_expense(request):        
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
        form = TransactionIncomeForm(request.POST)
        if form.is_valid():

            # get the user account category
            user = request.user            
            account_category = AccountCategory.objects.get(user=user)
           
            # create transaction with the acount category
            transaction = form.save(commit=False)
            transaction.user = user
            transaction.account_category = account_category            
            form.save()       
            return redirect('index')
    else:
        form = TransactionIncomeForm()
    context = {
        'form': form
    }           
    return render(request, 'trackerapp/add_income.html', context)


def transactions(request):                      # check all views below for user authentication
    # filter by month
    year = datetime.datetime.now().year
    month_choices = [
        (1, 'January'), 
        (2, 'February'), 
        (3, 'March'), 
        (4, 'April'),
        (5, 'May'), 
        (6, 'June'), 
        (7, 'July'), 
        (8, 'August'),
        (9, 'September'), 
        (10, 'October'), 
        (11, 'November'), 
        (12, 'December')
    ]

    transactions = Transactions.objects.all()

    if request.method == 'POST':
        month = int(request.POST.get('month'))
        transactions = transactions.filter(
            Q(transaction_date__year=year) & Q(transaction_date__month=month)
        )
      
    return render(request, 'trackerapp/transactions.html', {'transactions': transactions, 'month_choices': month_choices})


def categories(request):
    categories = ExpenseCategory.objects.all()
    return render(request, 'trackerapp/categories.html', {'categories': categories})


def categories_add(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            # retrieve input data
            custom_category_name = form.cleaned_data['custom_category_name']
            category = ExpenseCategory(user=request.user, category_name = custom_category_name)
            category.save()            
            return redirect('categories')
    else:
        form = AddCategoryForm()

    return render(request, 'trackerapp/categories_add.html', {'form': form})

# does not work, needs fixing
def categories_edit(request, category_id):
    category = get_object_or_404(ExpenseCategory, id=category_id, user=request.user)

    if request.method == 'POST':
        form = EditCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()            
            return redirect('categories')
    else:
        form = EditCategoryForm(instance=category)
    return render(request, 'trackerapp/categories_edit.html', {'form': form})


def categories_delete(request, category_id):
    category = get_object_or_404(ExpenseCategory, id=category_id, user=request.user)
    category.delete()
    return redirect('categories')

# -------------------postponed
def accounts(request):
    accounts = AccountCategory.objects.all()
    return render(request, 'trackerapp/accounts.html', {'accounts': accounts})


# Charts.js

def expenses_by_category(request):
    expense_categories = ExpenseCategory.objects.filter(user=request.user)

    category_label = [category.category_name for category in expense_categories]

    total_expense = []
    for category in expense_categories:
        transactions = Transactions.objects.filter(user=request.user, expense_categories=category)
        category_total = sum(transaction.amount for transaction in transactions)
        total_expense.append(category_total)

    return render(request, 'trackerapp/index.html', {'category_label': category_label, 'total_expense': total_expense})

        




    




            



