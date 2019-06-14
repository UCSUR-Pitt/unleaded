from django.contrib import admin
from .models import PipeRecord, PipePicture



class PipeRecordAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'home', 'step1', 'step2', 'step3', 'step4',
                    'step5', 'step6']
    readonly_fields = ('picture',)

    search_fields = list_display
    ordering = ['-created_at']


admin.site.register(PipeRecord, PipeRecordAdmin)


class PipePictureAdmin(admin.ModelAdmin):
    fields = ('image', 'img')
    readonly_fields = ('img',)
    list_display = ['image', 'img']
    pass


admin.site.register(PipePicture, PipePictureAdmin)
