from datetime import date, timedelta
from tabnanny import check


def calculate_date_intervals(start_date, end_date, days_or_months):
	if days_or_months == "days":
		return (end_date - start_date).days

	elif days_or_months == "months":
		result = (end_date.year - start_date.year) * 12
		result += (end_date.month - start_date.month)
		if end_date.day < start_date.day:
			result -= 1
		return result

	else:
		raise Exception("days_or_months can only be 'days' or 'months'")


def add_interval_to_date(original_date, days_or_months, value):
	if days_or_months == "days":
		return original_date + timedelta(days = value)

	elif days_or_months == "months":
		year, month = divmod(original_date.month + value, 12) # original_date.month + value // 12 | original_date.month + value % 12.
		if month == 0:
			month = 12
			# year = year - 1
			year -= 1

		year += original_date.year
		day = original_date.day
		return date(year, month, day)

	else:
		raise Exception("days_or_months can only be 'days' or 'months'")

def calculate_total_repetition(obj, last_balance_date, today, result_dict = None):
	total = 0
	repetition_time = obj.repetition_time
	end_date = obj.repetition_end if obj.repetition_end else today
	if obj.repetition_interval == 2: # interval == days
		days_or_months = "days"

	elif obj.repetition_interval == 3: # interval == weeks
		# repetition_time = repetition_time * 7
		repetition_time *= 7
		days_or_months = "days"

	elif obj.repetition_interval == 4: # interval == months
		days_or_months = "months"

	elif obj.repetition_interval == 5: # interval == years
		# repetition_time = repetition_time * 12
		repetition_time *= 12
		days_or_months = "months"

	else:
		raise Exception("repetition interval can only be between 2 to 5 included")

	balance_to_obj_time = calculate_date_intervals(obj.date, last_balance_date, days_or_months)
	if balance_to_obj_time <= 0:
		check_date = obj.date

	else:
		num_of_intervals_before = int(balance_to_obj_time / repetition_time)
		check_date = add_interval_to_date(obj.date, days_or_months, repetition_time * num_of_intervals_before)

	while last_balance_date >= check_date:
		check_date = add_interval_to_date(check_date, days_or_months, repetition_time)

	while check_date <= end_date:
		if result_dict is None:
			total += obj.value

		else:
			result_dict[str(check_date)] = obj.value if str(check_date) not in result_dict else result_dict[str(check_date)] + obj.value

		check_date = add_interval_to_date(check_date, days_or_months, repetition_time)

	return total if result_dict is None else result_dict