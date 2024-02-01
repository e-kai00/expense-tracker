from django.test import TestCase
from django.contrib.auth.models import User
from trackerapp.models import Transactions, ExpenseCategory


class TestTransactions(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test-user', password='test-password')
        self.expense_category = ExpenseCategory.objects.create(user=self.user, category_name='Fitness')

    def test_create_expense_transaction(self):
        transaction = Transactions.objects.create(
            user=self.user,
            expense_category = self.expense_category,
            amount=100,
            transaction_type='Expense'            
        )

        self.assertEqual(transaction.user, self.user)
        self.assertEqual(transaction.expense_category, self.expense_category)
        self.assertEqual(transaction.amount, 100)
        self.assertEqual(transaction.transaction_type, 'Expense')
