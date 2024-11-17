from django.contrib import admin
from .models import Income, Outcome, Balance

# Register your models here.
class IncomeOutcomeAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': ('user', 'type', 'value', 'date')
		}),
		(None, {
			'fields': ('created_at', 'updated_at'),
			'classes': ('collapse',),
		}),
	)
	readonly_fields = ('created_at', 'updated_at')

# class OutcomeAdmin(admin.ModelAdmin):
# 	fieldsets = (
# 		(None, {
# 			'fields': ('name', 'description', 'user')
# 		}),
# 		(None, {
# 			'fields': ('created_at', 'updated_at'),
# 			'classes': ('collapse',),
# 		}),
# 	)
# 	readonly_fields = ('created_at', 'updated_at')

admin.site.register(Income, IncomeOutcomeAdmin)
admin.site.register(Outcome)
admin.site.register(Balance)