from django.shortcuts import render, redirect, get_object_or_404
from .forms import TransactionForm
from .models import Transactions
from django.http import HttpResponse
from django.db.models.functions import TruncMonth
from django.db.models import Sum
from collections import defaultdict
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import csv


@login_required
def add_transaction(request):
    form = TransactionForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        transaction = form.save(commit=False)
        transaction.user = request.user
        transaction.save()
        return redirect('add_transaction')
    
    selected_category = request.GET.get('category')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    
    transactions = Transactions.objects.filter(user=request.user).order_by('-date')

    if selected_category and selected_category.lower() != "none":
        transactions = transactions.filter(category__icontains=selected_category)
    
    if start_date:
        transactions = transactions.filter(date__gte=start_date)
    if end_date:
        transactions = transactions.filter(date__lte=end_date)

    paginator = Paginator(transactions, 5)
    page_number = request.GET.get('page')
    transactions = paginator.get_page(page_number)

    income_total = sum(t.amount for t in transactions if t.transaction_type == 'income')
    expense_total = sum(t.amount for t in transactions if t.transaction_type == 'expense')
    balance = income_total - expense_total

    categories = Transactions.objects.filter(user=request.user).values_list('category', flat=True).distinct()

    # ✅ Monthly Summary
    monthly_summary = (
        Transactions.objects.filter(user=request.user)
        .annotate(month=TruncMonth('date'))
        .values('month', 'transaction_type')
        .annotate(total=Sum('amount'))
        .order_by('-month')
    )

    summary_data = defaultdict(lambda: {'income': 0, 'expense': 0, 'balance': 0})
    for entry in monthly_summary:
        month = entry['month'].strftime('%B %Y')
        if entry['transaction_type'] == 'income':
            summary_data[month]['income'] = entry['total']
        else:
            summary_data[month]['expense'] = entry['total']
        summary_data[month]['balance'] = (
            summary_data[month]['income'] - summary_data[month]['expense']
        )

    context = {
        'form': form,
        'transactions': transactions,
        'paginator': paginator,
        'income_total': income_total,
        'expense_total': expense_total,
        'balance': balance,
        'selected_category': selected_category,
        'categories': categories,
        'start_date': start_date,
        'end_date': end_date,
        'summary_data': dict(summary_data),
    }

    return render(request, 'tracker/add_transaction.html', context)


@login_required
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="transactions.csv"'

    writer = csv.writer(response)
    writer.writerow(['Date', 'Title', 'Amount', 'Type', 'Category'])

    for t in Transactions.objects.filter(user=request.user):
        writer.writerow([t.date, t.title, t.amount, t.transaction_type, t.category])

    return response


@login_required
def export_monthly_summary(request):
    monthly_summary = (
        Transactions.objects.filter(user=request.user)
        .annotate(month=TruncMonth('date'))
        .values('month', 'transaction_type')
        .annotate(total=Sum('amount'))
        .order_by('-month')
    )

    summary_data = defaultdict(lambda: {'income': 0, 'expense': 0, 'balance': 0})
    for entry in monthly_summary:
        month = entry['month'].strftime('%B %Y')
        if entry['transaction_type'] == 'income':
            summary_data[month]['income'] = entry['total']
        else:
            summary_data[month]['expense'] = entry['total']
        summary_data[month]['balance'] = (
            summary_data[month]['income'] - summary_data[month]['expense']
        )

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="monthly_summary.csv"'

    writer = csv.writer(response)
    writer.writerow(['Month', 'Total Income', 'Total Expense', 'Balance'])

    for month, data in summary_data.items():
        writer.writerow([
            month,
            round(data['income'], 2),
            round(data['expense'], 2),
            round(data['balance'], 2)
        ])

    return response


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('add_transaction')
    else:
        form = UserCreationForm()
    return render(request, 'tracker/register.html', {'form': form})


@login_required
def edit_transaction(request, pk):
    transaction = get_object_or_404(Transactions, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('add_transaction')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'tracker/edit_transaction.html', {'form': form})


@login_required
def delete_transaction(request, pk):
    transaction = get_object_or_404(Transactions, pk=pk, user=request.user)
    if request.method == 'POST':
        transaction.delete()
        return redirect('add_transaction')
    return render(request, 'tracker/delete_transaction.html', {'transaction': transaction})
