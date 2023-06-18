from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add_expense', views.add_expense, name='add_expense'),
    path('add_income', views.add_income, name='add_income'),
    path('transactions', views.transactions, name='transactions'),
    path('categories', views.categories, name='categories'),
    path('categories_add', views.categories_add, name='categories_add'),
    path('categories/edit/<int:category_id>/', views.categories_edit, name='categories_edit'),
    path('categories/delete/<int:category_id>/', views.categories_delete, name='categories_delete'),
    path('accounts', views.accounts, name='accounts'),
    path('api-data/', views.expenses_by_category1, name='api-data'),
    
    
]