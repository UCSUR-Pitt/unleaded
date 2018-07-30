from django.contrib import admin

from .models import PipeRecord

class PipeRecordAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'home', 'step1', 'step2', 'step3', 'step4', 'step5', 'step6']

    search_fields = list_display
    ordering = ['created_at']

admin.site.register(PipeRecord, PipeRecordAdmin)
