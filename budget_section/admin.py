from django.contrib import admin
from .models import Budget, Category, Transaction, BudgetTransaction

# Register your models here.
class BudgetAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': ('name', 'amount', 'user', 'start_date', 'end_date', 'slug')
		}),
		(None, {
			'fields': ('created_at', 'updated_at'),
			'classes': ('collapse',),
		}),
	)
	readonly_fields = ('created_at', 'updated_at')

class CategoryAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': ('name', 'description', 'user')
		}),
		(None, {
			'fields': ('created_at', 'updated_at'),
			'classes': ('collapse',),
		}),
	)
	readonly_fields = ('created_at', 'updated_at')

admin.site.register(Budget, BudgetAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Transaction)
admin.site.register(BudgetTransaction)