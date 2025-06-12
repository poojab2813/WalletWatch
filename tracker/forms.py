from django import forms
from .models import Transactions

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['title', 'amount', 'transaction_type', 'category', 'date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a short title (e.g., Grocery, Rent)'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter amount (e.g., 45.00)'
            }),
            'transaction_type': forms.Select(attrs={
                'class': 'form-select'
            }),
            'category': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'category-input',
                'placeholder': 'Enter or select a category',
                'autocomplete': 'off'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }
        labels = {
            'title': 'Title',
            'amount': 'Amount',
            'transaction_type': 'Type',
            'category': 'Category',
            'date':'Date',
        }
