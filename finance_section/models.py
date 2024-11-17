from django.db import models
from django.conf import settings

# Create your models here.
class Income(models.Model):
	class IncomeType(models.IntegerChoices):
		SALARY = 1, "Salary"
		SAVINGS = 2, "Savings"
		BONUS = 3, "Bonus"
		GIFT = 4, "Gift"
		OTHER = 5, "Other"

	class RepetitionInterval(models.IntegerChoices):
		NA = 1, "N/A"
		DAY = 2, "Days"
		WEEK = 3, "Weeks"
		MONTH = 4, "Months"
		YEAR = 5, "Years"

	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "user_incomes")
	value = models.DecimalField(max_digits = 10, decimal_places = 2)
	type = models.PositiveSmallIntegerField(choices = IncomeType.choices)
	date = models.DateField()
	repetitive = models.BooleanField(default = False)
	repetition_interval = models.PositiveSmallIntegerField(choices = RepetitionInterval.choices, default = 1)
	repetition_time = models.PositiveSmallIntegerField(default = 0)
	repetition_end = models.DateField(null = True, blank = True)
	notes = models.TextField(null = True, blank = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return f"{self.get_type_display()} Income"

	class Meta:
		verbose_name_plural = "incomes"


class Outcome(models.Model):
	class OutcomeType(models.IntegerChoices):
		RENT = 1, "Rent"
		SAVINGS = 2, "Savings"
		BILLS = 3, "Bills"
		CAR = 4, "Car"
		TRAVEL = 5, "Travel"
		HEALTH = 6, "Health"
		GROCERIES = 7, "Groceries"
		ATTRACTIONS = 8, "Attractions"
		CLOTHES = 9, "Clothes"
		CHARITY = 10, "Charity"

	class RepetitionInterval(models.IntegerChoices):
		NA = 1, "N/A"
		DAY = 2, "Days"
		WEEK = 3, "Weeks"
		MONTH = 4, "Months"
		YEAR = 5, "Years"

	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "user_outcomes")
	value = models.DecimalField(max_digits = 10, decimal_places = 2)
	type = models.PositiveSmallIntegerField(choices = OutcomeType.choices)
	date = models.DateField()
	repetitive = models.BooleanField(default = False)
	repetition_interval = models.PositiveSmallIntegerField(choices = RepetitionInterval.choices, default = 1)
	repetition_time = models.PositiveSmallIntegerField(default = 0)
	repetition_end = models.DateField(null = True, blank = True)
	notes = models.TextField(null = True, blank = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return f"{self.get_type_display()} Outcome"

	class Meta:
		verbose_name_plural = "outcomes"


class Balance(models.Model):
	class BalanceType(models.IntegerChoices):
		CURRENT = 1, "Current"
		SAVINGS = 2, "Savings"

	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "user_balances")
	value = models.DecimalField(max_digits = 10, decimal_places = 2)
	type = models.PositiveSmallIntegerField(choices = BalanceType.choices)
	date = models.DateField()
	notes = models.TextField(null = True, blank = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return f"{self.get_type_display()} Balance"

	class Meta:
		verbose_name_plural = "balances"