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
   
   # filter choices for expense_category based on logged-in user
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

    # handle error for non-unique category name
    def clean_category_name(self):
        category_name = self.cleaned_data.get('category_name')

        if category_name:            
            if ExpenseCategory.objects.filter(user=self.request.user, category_name=category_name).exists():
                raise forms.ValidationError("Category with this name already exists.")

        return category_name


class EditCategoryForm(forms.ModelForm):
    
    class Meta:
        model = ExpenseCategory
        fields = ['category_name']

    # handle error for non-unique category name
    def clean_category_name(self):
        category_name = self.cleaned_data.get('category_name')

        if category_name:            
            if ExpenseCategory.objects.filter(user=self.request.user, category_name=category_name).exists():
                raise forms.ValidationError("Category with this name already exists.")

        return category_name
        

    



      
    




   
  
        
        