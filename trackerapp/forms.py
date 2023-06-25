from django import forms
from .models import Transactions, ExpenseCategory


class TransactionForm(forms.ModelForm):
    """
    Form for adding an expense.

    Allow the user to add an expense transaction with the required
    information, such as the amount, expense category and (optional)
    notes.
    The `expense_category` field is filtered based on the logged-in
    user, ensuring that only the user's own expense categories are
    available for selection.
    """

    expense_category = forms.ModelChoiceField(
        ExpenseCategory.objects.all(),
        empty_label=None,
    )

    transaction_type = forms.CharField(
        widget=forms.HiddenInput,
        initial='Expense'
    )

    # filter expense_category based on logged-in user
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.fields['expense_category'].queryset = (
            ExpenseCategory.objects.filter(user=user)
        )

    class Meta:
        model = Transactions
        fields = ['amount', 'expense_category', 'transaction_type', 'notes']


class TransactionIncomeForm(forms.ModelForm):
    """
    Form for adding an income.

    Allow the user to add an income transaction with the required
    information, such as the amount and (optional) notes.
    """

    transaction_type = forms.CharField(
        widget=forms.HiddenInput,
        initial='Income'
    )

    class Meta:
        model = Transactions
        fields = ['amount', 'transaction_type', 'notes']


class AddCategoryForm(forms.ModelForm):
    """
    Form for adding a new expense category.

    Allow the user to add a new expense category by specifying
    the category name. It will raise ValidationError, if the
    category name entered by the user already exists for
    the current user.
    """

    class Meta:
        model = ExpenseCategory
        fields = ['category_name']

    def clean_category_name(self):
        category_name = self.cleaned_data.get('category_name')

        if category_name:
            if ExpenseCategory.objects.filter(
                user=self.request.user,
                category_name=category_name
            ).exists():
                raise forms.ValidationError(
                    "This category is already exists.\
                        Enter another category name."
                )

        return category_name


class EditCategoryForm(forms.ModelForm):
    """
    Form for updating an expense category.

    Allow the user to edit an expense category by specifying
    a new category name. It will raise ValidationError, if the
    category name entered by the user already exists for
    the current user.
    """

    class Meta:
        model = ExpenseCategory
        fields = ['category_name']

    def clean_category_name(self):
        category_name = self.cleaned_data.get('category_name')

        if category_name:
            if ExpenseCategory.objects.filter(
                user=self.request.user,
                category_name=category_name
            ).exists():
                raise forms.ValidationError(
                    "This category is already exists.\
                        Enter another category name."
                )

        return category_name
