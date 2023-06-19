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

    class Meta:
        model = ExpenseCategory
        fields = ['category_name']

# does not work, needs fixing
class EditCategoryForm(forms.ModelForm):
    
    class Meta:
        model = ExpenseCategory
        fields = ['category_name']
      
    




   
  
        
        