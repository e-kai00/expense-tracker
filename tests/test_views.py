from django.test import TestCase
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.urls import reverse
from trackerapp.models import Transactions, ExpenseCategory
from datetime import date, timedelta


class TestTransactionModel(TestCase):
    """
    Test suite for the Transactions model.

    This class contains test cases to ensure the proper functioning of the Transactions model,
    which represents user's transactions - income and expenses.

    Test cases:
    1. 'test_create_expense_transaction': test the creation of an expense transaction.
    2. 'test_create_income_transaction': test the creation of an income transaction.
    """

    def setUp(self):
        self.user = User.objects.create_user(username='test-user', password='test-password')
        self.expense_category = ExpenseCategory.objects.create(user=self.user, category_name='Fitness')

    def test_create_expense_transaction(self):
        transaction = Transactions.objects.create(
            user=self.user,
            expense_category = self.expense_category,
            amount=100,
            transaction_type='Expense', 
            transaction_date=date.today(),
            notes='Test of expense notes'
        )

        self.assertEqual(transaction.user, self.user)
        self.assertEqual(transaction.expense_category, self.expense_category)
        self.assertEqual(transaction.amount, 100)
        self.assertEqual(transaction.transaction_type, 'Expense')
        self.assertEqual(transaction.transaction_date, date.today())
        self.assertEqual(transaction.notes, 'Test of expense notes')

    def test_create_income_transaction(self):
        transaction = Transactions.objects.create(
            user=self.user,
            amount=200,
            transaction_type='Income',
            transaction_date=date.today(),
            notes='Test of income notes'

        )

        self.assertEqual(transaction.user, self.user)
        self.assertIsNone(transaction.expense_category)
        self.assertEqual(transaction.amount, 200)
        self.assertEqual(transaction.transaction_type, 'Income')
        self.assertEqual(transaction.transaction_date, date.today())
        self.assertEqual(transaction.notes, 'Test of income notes')


class TestIndexView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test-user', password='test-password')
        self.client.login(username='test-user', password='test-password')
        self.expense_category_fitness = ExpenseCategory.objects.create(user=self.user, category_name='Fitness')
        self.expense_category_bills = ExpenseCategory.objects.create(user=self.user, category_name='Bills')


    def test_render_transactions(self):
        """
        - Create sample income and expense transactions.
        - Check that the rendered page contains the correct transaction details.
        - Verify that income transactions are summed up correctly.
        - Verify that expenses are categorized appropriately.
        - Confirm that the total balance is calculated and displayed accurately.
        """
        income_transaction_1 = Transactions.objects.create(
            user=self.user,
            amount=250,
            transaction_type='Income',
            transaction_date=date.today()
        )

        income_transaction_2 = Transactions.objects.create(
            user=self.user,
            amount=400,
            transaction_type='Income',
            transaction_date=date.today()
        )

        expense_transaction_1 = Transactions.objects.create(
            user=self.user,
            expense_category=self.expense_category_fitness,
            amount=50,
            transaction_type='Expense',
            transaction_date=date.today() - timedelta(days=2)
        )
        
        expense_transaction_2 = Transactions.objects.create(
            user=self.user,
            expense_category=self.expense_category_fitness,
            amount=100,
            transaction_type='Expense',
            transaction_date=date.today()
        )

        expense_transaction_3 = Transactions.objects.create(
            user=self.user,
            expense_category=self.expense_category_bills,
            amount=90,
            transaction_type='Expense',
            transaction_date=date.today()
        )

        response = self.client.get(reverse('index'))
            
        self.assertEqual(response.status_code, 200)
        # print(response.content)

        self.assertContains(response, 'Income: $650')
        self.assertContains(response, 'Fitness: $150')
        self.assertContains(response, 'Bills: $90')
        self.assertContains(response, 'Balance $410.00')

    
class TestExpenseCategories(TestCase):
    """
    Test suite for the ExpenseCategory model and related views.

    This class contains test cases to ensure the proper functioning of
    adding, uniqueness, and editing of expense categories.

    Test cases:
    1. 'test_add_category': test the creation of a new expense category.
    2. 'test_unique_category_per_user': test that categories with the same name
       cannot be added for the same user.
    3. 'test_edit_category': test the ability to edit an existing expense category.
    """
    
    def setUp(self):
        self.user = User.objects.create(username='test-user', password='test-password')
        self.client.force_login(self.user)
        self.expense_category = ExpenseCategory.objects.create(user=self.user, category_name='Fitness')

    def test_add_category(self):
        expense_category = ExpenseCategory.objects.create(
        user=self.user,
        category_name='Education'
        )

        self.assertEqual(expense_category.user, self.user)
        self.assertEqual(expense_category.category_name, 'Education')

    def test_unique_category_per_user(self):
        
        with self.assertRaises(IntegrityError):
            ExpenseCategory.objects.create(
            user=self.user,
            category_name='Fitness'
        )

    def test_edit_category(self):
        new_category_name = 'Bills'
        url = reverse('categories_edit', args=[self.expense_category.id])
        data = {'category_name': new_category_name}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

        edited_category = ExpenseCategory.objects.get(id=self.expense_category.id)
        self.assertEqual(edited_category.category_name, new_category_name)
        
