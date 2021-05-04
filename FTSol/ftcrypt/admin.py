from django.contrib import admin
from .models import FTCRYPT


class FTCRYPTAdmin(admin.ModelAdmin):
    fieldsets = [ ('File & Details', {'fields': ['postfile']}), ]
    list_display = ('id', 'postfile', 'insertedon',)
    list_filter = ['insertedon']
    search_fields = ['postfile', 'insertedon', ]


admin.site.register(FTCRYPT, FTCRYPTAdmin)
