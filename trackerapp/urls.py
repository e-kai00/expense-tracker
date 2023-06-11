from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add_expense', views.add_expense, name='add_expense'),
    path('add_income', views.add_income, name='add_income'),
    path('transactions', views.transactions, name='transactions'),
    
]