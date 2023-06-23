from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, F, Sum
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Transactions, ExpenseCategory
from .forms import TransactionForm, TransactionIncomeForm, AddCategoryForm, EditCategoryForm
import datetime

# --------------MAIN PAGE

@login_required
def index(request):
    # get the current month and year
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    
    transactions = Transactions.objects.filter(
        user=request.user,
        transaction_date__year=year,
        transaction_date__month=month
    )
        # group expenses by categories, accumulate income
    total_by_category = transactions.filter(
        transaction_type='Expense'
        ).values('expense_category__category_name'
        ).annotate(total_expenses=Sum('amount')
    )

    total_income = transactions.filter(
        transaction_type='Income'
        ).aggregate(total=Sum('amount'))['total'] or 0
        
        # tatal balance for month
    balance = 0   
    for transaction in transactions:
        if transaction.transaction_type == 'Income':
            balance += transaction.amount
        else:
            balance -= transaction.amount   
        
    context = {
        'transactions': transactions,
        'total_by_category': total_by_category,
        'total_income': total_income,
        'balance': balance        
    }
    return render(request, 'trackerapp/index.html', context)


@login_required
def add_expense(request):
    user = request.user       
    if request.method == 'POST':
        form = TransactionForm(request.POST, user=user)
        if form.is_valid():
                     
            # account_category = AccountCategory.objects.get(user=user)
            # account_category, created = AccountCategory.objects.get_or_create(user=user, account_name='my Cash', defaults={'balance': 0.0})

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
            # transaction.account_category = account_category
            transaction.expense_category = expense_category
            form.save()       
            return redirect('index')
    else:
        form = TransactionForm(user=user)
             
    return render(request, 'trackerapp/add_expense.html', {'form': form})


@login_required
def add_income(request):
    if request.method == 'POST':
        form = TransactionIncomeForm(request.POST)
        if form.is_valid():

            # get the user account category
            user = request.user            
            # account_category = AccountCategory.objects.get(user=user)
           
            # create transaction with the acount category
            transaction = form.save(commit=False)
            transaction.user = user
            # transaction.account_category = account_category            
            form.save()       
            return redirect('index')
    else:
        form = TransactionIncomeForm()
            
    return render(request, 'trackerapp/add_income.html', {'form': form})


# --------------FILTERS

@login_required
def transactions(request):
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
    
    transactions = Transactions.objects.filter(
        user=request.user).order_by(
        F('transaction_date').desc()
    )
    
    month = None
    selected_month = None

    if request.method == 'POST':
        month = int(request.POST.get('month'))
        transactions = transactions.filter(
            Q(transaction_date__year=year) & Q(transaction_date__month=month)
        )
    else:
        month = datetime.datetime.now().month

    for month_num, month_name in month_choices:
        if month_num == month:
            selected_month = month_name
      
    return render(request, 'trackerapp/transactions.html', {'transactions': transactions, 'month_choices': month_choices, 'selected_month': selected_month})


# --------------EXPENSE CATEGORIES

@login_required
def categories(request):
    categories = ExpenseCategory.objects.filter(user=request.user)
    return render(request, 'trackerapp/categories.html', {'categories': categories})


@login_required
def categories_add(request):
    user=request.user
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        form.request = request
        if form.is_valid():
            category = form.save(commit=False)
            category.user = user
            category.save()
            # retrieve url of previous page and redirect to it
            previous_page = request.POST.get('previous_page')
            return redirect(previous_page)        
    else:
        form = AddCategoryForm()
        form.request = request

    return render(request, 'trackerapp/categories_add.html', {'form': form})


@login_required
def categories_edit(request, category_id):
    category = get_object_or_404(ExpenseCategory, id=category_id, user=request.user)

    if request.method == 'POST':
        form = EditCategoryForm(request.POST, instance=category)
        form.request = request
        if form.is_valid():
            form.save()            
            return redirect('categories')
    else:
        form = EditCategoryForm(instance=category)
        form.request = request
    return render(request, 'trackerapp/categories_edit.html', {'form': form})


@login_required
def categories_delete(request, category_id):
    category = get_object_or_404(ExpenseCategory, id=category_id, user=request.user)
    category.delete()
    return redirect('categories')


# --------------ACCOUNT CATEGORIES -------postponed

# @login_required
# def accounts(request):
#     accounts = AccountCategory.objects.filter(user=request.user)
#     return render(request, 'trackerapp/accounts.html', {'accounts': accounts})


# @login_required
# def accounts_add(request):
#     if request.method == 'POST':
#         form = AddAccountsForm(request.POST)
#         if form.is_valid():
#             account = form.save(commit=False)
#             account.user = request.user
#             account.save()            
#             return redirect('accounts')
#     else:
#         form = AddAccountsForm()

#     return render(request, 'trackerapp/accounts_add.html', {'form': form})


# --------------Chart.js

@login_required
def expenses_by_category(request):
    user=request.user
    expense_categories = ExpenseCategory.objects.filter(user=user)

    category_label = [category.category_name for category in expense_categories]

    total_expense = []
    for category in expense_categories:
        transactions = Transactions.objects.filter(user=user, expense_category=category)
        category_total = sum(transaction.amount for transaction in transactions)
        total_expense.append(category_total)    

    context = {
        'category_label': category_label,
        'total_expense': total_expense,
    }

    return JsonResponse(context)



    




            



