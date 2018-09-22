from django.contrib import admin

# Register your models here.

from .models import Table1, Table2

# admin.site.register(Table1)
admin.site.register(Table2)

@admin.register(Table1)
class Table1Admin(admin.ModelAdmin):
    list_display = ('c_date','fname','email',)
    # readonly_fields, fields = ('fname',), ('c_date','fname','email')