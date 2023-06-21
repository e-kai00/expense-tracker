from django import forms
from .models import Transactions, ExpenseCategory, AccountCategory


class TransactionForm(forms.ModelForm):   

    expense_category = forms.ModelChoiceField(
        ExpenseCategory.objects.all(), 
        empty_label=None,         
    )
          
    transaction_type = forms.CharField(
        widget=forms.HiddenInput, 
        initial='Expense'
    ) 
   
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.fields['expense_category'].queryset = ExpenseCategory.objects.filter(user=user)

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


# class AddAccountsForm(forms.ModelForm):
#     class Meta:
#         model = AccountCategory
#         fields = ['account_name', 'balance']
      
    




   
  
        
        