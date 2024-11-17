from datetime import date, timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import IncomeForm, OutcomeForm, BalanceForm
from .date_intervals import calculate_total_repetition
from .models import Income, Outcome, Balance


# Create your views here.

@method_decorator(login_required, name = "dispatch")
class IncomeListView(ListView):
	model = Income
	template_name = 'finance_section/income_outcome_list.html'
	paginate_by = 100
	extra_context = {'list_what': 'Income'}

	def get_queryset(self):
		user = self.request.user
		return Income.objects.filter(user = user).order_by('-id')


@method_decorator(login_required, name = 'dispatch')
@method_decorator(csrf_protect, name = 'dispatch')
class IncomeCreateView(CreateView):
	model = Income
	form_class = IncomeForm
	template_name = 'finance_section/income_outcome_form.html'
	extra_context = {'header': 'Add Income'}

	def form_valid(self, form):
		self.object = form.save(commit = False)
		self.object.user = self.request.user
		self.object.save()
		return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		messages.add_message(self.request, messages.SUCCESS, "Income created successfully")
		return reverse_lazy('finance_section:income_list')


@method_decorator(login_required, name = 'dispatch')
@method_decorator(csrf_protect, name = 'dispatch')
class IncomeDetailView(DetailView):
	model = Income
	template_name = 'finance_section/income_outcome_detail.html'
	extra_context = {'detail_what': 'Income'}

	def get_queryset(self):
		user = self.request.user
		return Income.objects.filter(user = user)


@method_decorator(login_required, name = 'dispatch')
@method_decorator(csrf_protect, name = 'dispatch')
class IncomeDeleteView(DeleteView):
	model = Income
	template_name = 'finance_section/income_outcome_delete.html'
	extra_context = {'delete_what': 'Income'}

	def get_queryset(self):
		user = self.request.user
		return Income.objects.filter(user = user)

	def get_success_url(self):
		messages.add_message(self.request, messages.SUCCESS, "Income deleted successfully")
		return reverse_lazy('finance_section:income_list')


@method_decorator(login_required, name = 'dispatch')
@method_decorator(csrf_protect, name = 'dispatch')
class IncomeUpdateView(UpdateView):
	model = Income
	form_class = IncomeForm
	template_name = 'finance_section/income_outcome_form.html'
	extra_context = {'header': 'Update Income'}

	def get_queryset(self):
		user = self.request.user
		return Income.objects.filter(user = user)

	def get_success_url(self):
		messages.add_message(self.request, messages.SUCCESS, "Income updated successfully")
		return reverse('finance_section:income_list')


@method_decorator(login_required, name = "dispatch")
class OutcomeListView(ListView):
	model = Outcome
	template_name = 'finance_section/income_outcome_list.html'
	paginate_by = 100
	extra_context = {'list_what': 'Outcome'}

	def get_queryset(self):
		user = self.request.user
		return Outcome.objects.filter(user = user).order_by('-id')


@method_decorator(login_required, name = 'dispatch')
@method_decorator(csrf_protect, name = 'dispatch')
class OutcomeCreateView(CreateView):
	model = Outcome
	form_class = OutcomeForm
	template_name = 'finance_section/income_outcome_form.html'
	extra_context = {'header': 'Add Outcome'}

	def form_valid(self, form):
		self.object = form.save(commit = False)
		self.object.user = self.request.user
		self.object.save()
		return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		messages.add_message(self.request, messages.SUCCESS, "Outcome created successfully")
		return reverse_lazy('finance_section:outcome_list')


@method_decorator(login_required, name = 'dispatch')
@method_decorator(csrf_protect, name = 'dispatch')
class OutcomeDetailView(DetailView):
	model = Outcome
	template_name = 'finance_section/income_outcome_detail.html'
	extra_context = {'detail_what': 'Outcome'}

	def get_queryset(self):
		user = self.request.user
		return Outcome.objects.filter(user = user)


@method_decorator(login_required, name = 'dispatch')
@method_decorator(csrf_protect, name = 'dispatch')
class OutcomeDeleteView(DeleteView):
	model = Outcome
	template_name = 'finance_section/income_outcome_delete.html'
	extra_context = {'delete_what': 'Outcome'}

	def get_queryset(self):
		user = self.request.user
		return Outcome.objects.filter(user = user)

	def get_success_url(self):
		messages.add_message(self.request, messages.SUCCESS, "Outcome deleted successfully")
		return reverse_lazy('finance_section:outcome_list')


@method_decorator(login_required, name = 'dispatch')
@method_decorator(csrf_protect, name = 'dispatch')
class OutcomeUpdateView(UpdateView):
	model = Outcome
	form_class = OutcomeForm
	template_name = 'finance_section/income_outcome_form.html'
	extra_context = {'header': 'Update Outcome'}

	def get_queryset(self):
		user = self.request.user
		return Outcome.objects.filter(user = user)

	def get_success_url(self):
		messages.add_message(self.request, messages.SUCCESS, "Outcome updated successfully")
		return reverse('finance_section:outcome_list')


@method_decorator(login_required, name = "dispatch")
class BalanceListView(ListView):
	model = Balance
	template_name = 'finance_section/income_outcome_list.html'
	paginate_by = 100
	extra_context = {'list_what': 'Balance'}

	def get_queryset(self):
		user = self.request.user
		return Balance.objects.filter(user = user).order_by('-id')


@method_decorator(login_required, name = 'dispatch')
@method_decorator(csrf_protect, name = 'dispatch')
class BalanceCreateView(CreateView):
	model = Balance
	form_class = BalanceForm
	template_name = 'finance_section/income_outcome_form.html'
	extra_context = {'header': 'Add Balance'}

	def form_valid(self, form):
		self.object = form.save(commit = False)
		self.object.user = self.request.user
		self.object.save()
		return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		messages.add_message(self.request, messages.SUCCESS, "Balance created successfully")
		return reverse_lazy('finance_section:balance_list')


@method_decorator(login_required, name = 'dispatch')
@method_decorator(csrf_protect, name = 'dispatch')
class BalanceDetailView(DetailView):
	model = Balance
	template_name = 'finance_section/income_outcome_detail.html'
	extra_context = {'detail_what': 'Balance'}

	def get_queryset(self):
		user = self.request.user
		return Balance.objects.filter(user = user)


@method_decorator(login_required, name = 'dispatch')
@method_decorator(csrf_protect, name = 'dispatch')
class BalanceDeleteView(DeleteView):
	model = Balance
	template_name = 'finance_section/income_outcome_delete.html'
	extra_context = {'delete_what': 'Balance'}

	def get_queryset(self):
		user = self.request.user
		return Balance.objects.filter(user = user)

	def get_success_url(self):
		messages.add_message(self.request, messages.SUCCESS, "Balance deleted successfully")
		return reverse_lazy('finance_section:balance_list')


@method_decorator(login_required, name = 'dispatch')
@method_decorator(csrf_protect, name = 'dispatch')
class BalanceUpdateView(UpdateView):
	model = Balance
	form_class = BalanceForm
	template_name = 'finance_section/income_outcome_form.html'
	extra_context = {'header': 'Update Balance'}

	def get_queryset(self):
		user = self.request.user
		return Balance.objects.filter(user = user)

	def get_success_url(self):
		messages.add_message(self.request, messages.SUCCESS, "Balance updated successfully")
		return reverse_lazy('finance_section:balance_list')


@login_required
def current_period(request):
	make_calls = True
	income_types = Income.IncomeType.choices
	outcome_types = Outcome.OutcomeType.choices
	last_balance = Balance.objects.filter(user = request.user, type = 1).order_by('-date').first()
	if not last_balance:
		messages.add_message(request, messages.WARNING, "No 'current' balance has been recorded.\nPlease add at least one 'current' balance record.")
		make_calls = False
		context = {'make_calls': make_calls}
	else:
		total_income = (Income.objects.filter(user = request.user, date__gt = last_balance.date, date__lte = date.today(), repetitive = False).aggregate(total = Sum('value'))[
			                'total']
		                or 0)
		total_outcome = (Outcome.objects.filter(user = request.user, date__gt = last_balance.date, date__lte = date.today(), repetitive = False).aggregate(total = Sum('value'))[
			                 'total']
		                 or 0)

		incomes = Income.objects.filter(user = request.user, repetitive = True)
		outcomes = Outcome.objects.filter(user = request.user, repetitive = True)
		for income in incomes:
			total_income += calculate_total_repetition(income, last_balance.date, date.today())
		for outcome in outcomes:
			total_outcome += calculate_total_repetition(outcome, last_balance.date, date.today())

		estimated_balance_now = last_balance.value + total_income - total_outcome

		context = {
			'make_calls': make_calls,
			'last_balance_check': last_balance,
			'estimated_balance_now': estimated_balance_now,
			'estimated_income': total_income,
			'estimated_outcome': total_outcome,
			'income_types': income_types,
			'outcome_types': outcome_types,
		}
	return render(request, 'finance_section/current_period.html', context)


@login_required
def year_overview(request):
	make_calls = True
	last_balance = Balance.objects.filter(user = request.user, type = 1).order_by('-date').first()
	last_savings_balance = Balance.objects.filter(user = request, type = 2).order_by('-date').first()
	if not last_balance and not last_savings_balance:
		messages.add_message(request, messages.WARNING, "No 'current' balance has been recorded.\nPlease add at least one 'current' balance record.")
		make_calls = False
	context = {'make_calls': make_calls}
	return render(request, 'finance_section/year_overview.html', context)


@login_required
def get_summary_tiles(request):
	today = date.today()
	last_balance = Balance.objects.filter(user = request.user, type = 1).order_by('-date').first()
	if not last_balance:
		return JsonResponse({"error": "No 'current' balance has been recorded.\nPlease add at least one 'current' balance record."})
	total_income = Income.objects.filter(user = request.user, date__gt = last_balance.date, date__lte = today, repetitive = False).aggregate(total = Sum('value'))['total']
	# date__gt = date_greater_than | date__lte = date_less_than_equal
	total_income = 0 if not total_income else total_income
	total_outcome = Outcome.objects.filter(user = request.user, date__gt = last_balance.date, date__lte = today, repetitive = False).aggregate(total = Sum('value'))['total']
	total_outcome = 0 if not total_outcome else total_outcome

	incomes = Income.objects.filter(user = request.user, repetitive = True)
	outcomes = Outcome.objects.filter(user = request.user, repetitive = True)
	for income in incomes:
		total_income += calculate_total_repetition(income, last_balance.date, today)
	for outcome in outcomes:
		total_outcome += calculate_total_repetition(outcome, last_balance.date, today)

	return JsonResponse(
		{
			"last_balance_value": last_balance.value,
			"last_balance_date": last_balance.date,
			"estimated_balance": last_balance.value + total_income - total_outcome,
			"total_income": total_income,
			"total_outcome": total_outcome
		}
	)


@login_required
def get_year_chart(request):
	balance_type = request.GET.get('balance_type')
	if balance_type not in ['current', 'savings']:
		return JsonResponse({"error": "Please specify the balance type to 'current' or 'savings'."})

	today = date.today()
	begin_of_year = date(today.year, 1, 1)
	end_of_year = date(today.year, 12, 28)

	balance = Balance.objects.filter(user = request.user, type = 1 if balance_type == "current" else 2, date__lte = begin_of_year).order_by('-date').first()
	if not balance:
		balance = Balance.objects.filter(user = request.user, type = 1 if balance_type == "current" else 2, date__lte = begin_of_year).order_by('date').first()
		if not balance:
			return JsonResponse({"error": "No 'current' balance has been recorded.\nPlease add at least one 'current' balance record."})

	balance_checks = {}
	income_per_day = {}
	outcome_per_day = {}

	balances = Balance.objects.filter(user = request.user, type = 1 if balance_type == 'current' else 2, date__gte = balance.date)
	for bal in balances:
		balance_checks[str(bal.date)] = bal.value

	if balance_type == "current":
		for income in Income.objects.filter(user = request.user, date__gte = balance.date, repetitive = False):
			income_per_day[str(income.date)] = income.value if str(income.date) not in income_per_day else income_per_day[str(income.date)] + income.value
		for outcome in Outcome.objects.filter(user = request.user, date__gte = balance.date, repetitive = False):
			outcome_per_day[str(outcome.date)] = outcome.value if str(outcome.date) not in outcome_per_day else outcome_per_day[str(outcome.date)] + outcome.value

		for income in Income.objects.filter(user = request.user, repetitive = True):
			calculate_total_repetition(income, balance.date, end_of_year, income_per_day)

		for outcome in Outcome.objects.filter(user = request.user, repetitive = True):
			calculate_total_repetition(outcome, balance.date, end_of_year, outcome_per_day)

	else:
		for income in Income.objects.filter(user = request.user, date__gte = balance.date, type = 2, repetitive = False):
			outcome_per_day[str(income.date)] = income.value if str(income.date) not in outcome_per_day else outcome_per_day[str(income.date)] + income.value

		for outcome in Outcome.objects.filter(user = request.user, date__gte = balance.date, type = 2, repetitive = False):
			income_per_day[str(outcome.date)] = outcome.value if str(outcome.date) not in income_per_day else income_per_day[str(outcome.date)] + outcome.value

		for income in Income.objects.filter(user = request.user, type = 2, repetitive = True):
			calculate_total_repetition(income, balance.date, end_of_year, outcome_per_day)

		for outcome in Outcome.objects.filter(user = request.user, type = 2, repetitive = True):
			calculate_total_repetition(outcome, balance.date, end_of_year, income_per_day)

	labels = []
	data_estimated = []
	data_balance_check = []
	data_today = []
	date_marker = balance.date
	balance_on_marker_date = balance.value

	if date_marker > begin_of_year:
		fill_date_marker = date(today.year, 1, 1)
		while fill_date_marker < date_marker:
			labels.append(str(fill_date_marker))
			data_estimated.append(None)
			data_balance_check.append(None)
			data_today.append(None)
			fill_date_marker += timedelta(days = 1)
	else:
		while date_marker < begin_of_year:
			balance_on_marker_date += income_per_day.get(str(date_marker), 0)
			balance_on_marker_date -= outcome_per_day.get(str(date_marker), 0)
			date_marker += timedelta(days = 1)

	while date_marker <= end_of_year:
		labels.append(str(date_marker))
		if str(date_marker) in balance_checks:
			balance_on_marker_date = balance_checks[str(date_marker)]
			data_balance_check.append(balance_checks[str(date_marker)])
		else:
			balance_on_marker_date += income_per_day.get(str(date_marker), 0)
			balance_on_marker_date -= outcome_per_day.get(str(date_marker), 0)
			data_balance_check.append(None)
		data_estimated.append(balance_on_marker_date)
		if date_marker == today:
			data_today.append(balance_on_marker_date)
		else:
			data_today.append(None)
		date_marker += timedelta(days = 1)

	return JsonResponse(
		{
			"labels": labels,
			"data_estimated": data_estimated,
			"data_balance_check": data_balance_check,
			"data_today": data_today
		}
	)


@login_required
def get_income_or_outcome_by_type(request):
	get_what = request.GET.get('get_what')
	summary_type = request.GET.get('summary_type')
	type_filter = request.GET.get('type', 'all')

	if get_what is None or get_what not in ['income', 'outcome']:
		return JsonResponse({'error': 'Please specify get_what parameter to be either "income" or "outcome".'})

	if get_what == 'income':
		obj = Income
		obj_types = Income.IncomeType
	else:
		obj = Outcome
		obj_types = Outcome.OutcomeType

	today = date.today()
	if summary_type == 'current_period':
		last_balance = Balance.objects.filter(user = request.user, type = 1).order_by('-date').first()
		if not last_balance:
			return JsonResponse({'error': 'No current balance has been recorded. Please add at least one current balance record.'})
		start_date = last_balance.date
		end_date = today
	elif summary_type == 'year_overview':
		start_date = date(today.year - 1, 12, 31)
		end_date = date(today.year, 12, 31)
	else:
		return JsonResponse({'error': 'Please specify summary_type parameter to be either "current_period" or "year_overview".'})

	labels = []
	data = []
	for obj_type in obj_types.choices:
		if type_filter != 'all' and obj_type[0] != type_filter:
			continue
		labels.append(obj_type[1])
		total = obj.objects.filter(
			user = request.user, type = obj_type[0], date__gt = start_date,
			date__lte = end_date, repetitive = False
			).aggregate(total = Sum('value'))['total']
		total = 0 if total is None else total

		for o in obj.objects.filter(user = request.user, type = obj_type[0], repetitive = True):
			total += calculate_total_repetition(o, start_date, end_date)
		data.append(total)

	return JsonResponse({'labels': labels, 'data': data})