from django.urls import path
from finance_section import views

# TODO: Continue working on the budget section

app_name = "finance_section"

urlpatterns = [
	path('income_list/', views.IncomeListView.as_view(), name = 'income_list'),
	path('income_details/<pk>', views.IncomeDetailView.as_view(), name = 'income_details'),
	path('income_create/', views.IncomeCreateView.as_view(), name = 'income_create'),
	path('income_delete/<pk>/', views.IncomeDeleteView.as_view(), name = 'income_delete'),
	path('income_update/<pk>/', views.IncomeUpdateView.as_view(), name='income_update'),

	path('outcome_list/', views.OutcomeListView.as_view(), name = 'outcome_list'),
	path('outcome_details/<pk>/', views.OutcomeDetailView.as_view(), name = 'outcome_details'),
	path('outcome_create/', views.OutcomeCreateView.as_view(), name = 'outcome_create'),
	path('outcome_delete/<pk>/', views.OutcomeDeleteView.as_view(), name = 'outcome_delete'),
	path('outcome_update/<pk>/', views.OutcomeUpdateView.as_view(), name='outcome_update'),

	path('balance_list/', views.BalanceListView.as_view(), name = 'balance_list'),
	path('balance_details/<pk>/', views.BalanceDetailView.as_view(), name = 'balance_details'),
	path('balance_create/', views.BalanceCreateView.as_view(), name = 'balance_create'),
	path('balance_delete/<pk>/', views.BalanceDeleteView.as_view(), name = 'balance_delete'),
	path('balance_update/<pk>/', views.BalanceUpdateView.as_view(), name='balance_update'),

	path('current_period/', views.current_period, name = 'current_period'),
	path('year_overview/', views.year_overview, name = 'year_overview'),
	path('get_summary_tiles/', views.get_summary_tiles, name = 'get_summary_tiles'),
	path('get_year_chart/', views.get_year_chart, name = 'get_year_chart'),
	path('get_income_or_outcome_by_type/', views.get_income_or_outcome_by_type, name = 'get_income_or_outcome_by_type'),
]