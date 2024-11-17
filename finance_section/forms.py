from datetime import date
from django import forms
from .models import Income, Outcome, Balance

class DateInput(forms.DateInput):
	input_type = "date"

class IncomeOutcomeForm(forms.ModelForm):
	def is_valid(self):
		is_valid = super().is_valid()

		value = self.cleaned_data.get("value")
		form_date = self.cleaned_data.get("date")
		repetitive = self.cleaned_data.get("repetitive")
		repetition_interval = self.cleaned_data.get("repetition_interval")
		repetition_time = self.cleaned_data.get("repetition_time")
		repetition_end = self.cleaned_data.get("repetition_end")

		if value <= 0:
			self.add_error(field = "value", error = "Value must be positive.")
			is_valid = False

		if repetition_interval == 4 and form_date.day > 28:
			self.add_error(field = "date", error = "Day cannot exceed 28.")
			is_valid = False

		if repetitive:
			if repetition_interval == 1:
				self.add_error(field = "repetition_interval", error = "Repetition interval cannot be N/A if Repetition is selected.")
				is_valid = False
			if repetition_time == 0:
				self.add_error(field = "repetition_time", error = "Repetition time cannot be 0 if Repetition is selected.")
				is_valid = False
			if form_date and repetition_end:
				if repetition_end <= form_date:
					self.add_error(field = "repetition_end", error = "Repetition end date cannot be earlier than today.")
					is_valid = False

		else:
			if repetition_interval != 1:
				self.add_error(field = "repetition_interval", error = "Repetitive must be selected when Repetition interval is not N/A.")
				is_valid = False
			if repetition_time != 0:
				self.add_error(field = "repetition_time", error = "Repetitive must be selected when Repetition time is not 0.")
				is_valid = False
			if repetition_end:
				self.add_error(field = "repetition_end", error = "Repetitive must be selected when Repetition end date is not empty.")
				is_valid = False

		return is_valid

class IncomeForm(IncomeOutcomeForm):
	class Meta:
		model = Income
		fields = ["value", "type", "date", 'repetitive', 'repetition_interval', 'repetition_time', 'repetition_end', "notes"]

	date = forms.DateField(widget = DateInput, initial = date.today())
	repetition_end = forms.DateField(widget = DateInput, required = False)


class OutcomeForm(IncomeOutcomeForm):
	class Meta:
		model = Outcome
		fields = ["value", "type", "date", 'repetitive', 'repetition_interval', 'repetition_time', 'repetition_end', "notes"]

	date = forms.DateField(widget = DateInput, initial = date.today())
	repetition_end = forms.DateField(widget = DateInput, required = False)

class BalanceForm(forms.ModelForm):
	class Meta:
		model = Balance
		fields = ["value", "type", "date", "notes"]

	date = forms.DateField(widget = DateInput, initial = date.today())