from django import forms
from .models import Transactions, ExpenseCategory


class TransactionForm(forms.ModelForm):

    expense_category = forms.ModelChoiceField(
        ExpenseCategory.objects.all(), 
        empty_label=None, 
        # widget=forms.Select(choices=ExpenseCategory.CATEGORIES)
    )

    # expense_category = forms.ChoiceField(required=False, choices=ExpenseCategory.CATEGORIES) 

    class Meta:
        model = Transactions
        fields = ['amount', 'expense_category', 'notes']    

    

   
  
        
        