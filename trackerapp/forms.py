from django import forms
from .models import Transactions, ExpenseCategory


class TransactionForm(forms.ModelForm):

    expense_category = forms.ModelChoiceField(
        ExpenseCategory.objects.all(), 
        empty_label=None,         
    )
          
    transaction_type = forms.CharField(
        widget=forms.HiddenInput, 
        initial='Expense'
    )
   
    class Meta:
        model = Transactions
        fields = ['amount', 'expense_category', 'transaction_type', 'notes']


class TransactionIncomeForm(forms.ModelForm):

    transaction_type = forms.CharField(
        widget=forms.HiddenInput, 
        initial='Income'
    )

    class Meta:
        model = Transactions
        fields = ['amount', 'transaction_type', 'notes']


class AddCategoryForm(forms.ModelForm):

    custom_category_name = forms.CharField(max_length=200, label='Custom Category Name')

    class Meta:
        model = ExpenseCategory
        fields = ['custom_category_name']
    

   
  
        
        