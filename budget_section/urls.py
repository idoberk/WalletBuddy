from django.urls import path
# from budget_section.views import (BudgetListView, BudgetDetailView, BudgetCreateView, BudgetDeleteView, BudgetUpdateView,
#                                   CategoryListView, CategoryDetailView, CategoryCreateView, CategoryDeleteView, CategoryUpdateView,
#                                   TransactionListView, TransactionDetailView, TransactionCreateView, TransactionDeleteView, TransactionUpdateView,
#                                   SummaryTiles)

from budget_section import views

# TODO: Continue working on the budget section

app_name = "budget_section"

urlpatterns = [
	path('budgets/', views.BudgetListView.as_view(), name = 'budget_list'),
	path('budget/detail/<slug:slug>/', views.BudgetDetailView.as_view(), name = 'budget_details'),
	path('budget/create/', views.BudgetCreateView.as_view(), name = 'budget_create'),
	path('budget/delete/<slug:slug>/', views.BudgetDeleteView.as_view(), name = 'budget_delete'),
	path('budget/update/<slug:slug>/', views.BudgetUpdateView.as_view(), name='budget_update'),

	path('categories/', views.CategoryListView.as_view(), name = 'category_list'),
	path('category/detail/<slug:slug>/', views.CategoryDetailView.as_view(), name = 'category_details'),
	path('category/create/', views.CategoryCreateView.as_view(), name = 'category_create'),
	path('category/delete/<slug:slug>/', views.CategoryDeleteView.as_view(), name = 'category_delete'),
	path('category/update/<slug:slug>/', views.CategoryUpdateView.as_view(), name='category_update'),

	path('transactions/', views.TransactionListView.as_view(), name = 'transaction_list'),
	path('transaction/detail/<slug:slug>/', views.TransactionDetailView.as_view(), name = 'transaction_details'),
	path('transaction/create/', views.TransactionCreateView.as_view(), name = 'transaction_create'),
	path('transaction/delete/<slug:slug>/', views.TransactionDeleteView.as_view(), name = 'transaction_delete'),
	path('transaction/update/<slug:slug>/', views.TransactionUpdateView.as_view(), name='transaction_update'),

	path('budget/current_period/budget_name/<slug:slug>', views.SummaryTiles.as_view(), name='budget_summary'),
]