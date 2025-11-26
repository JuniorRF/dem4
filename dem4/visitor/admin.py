from django.contrib import admin
from .models import Visitor

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('user','ip_address', 'path', 'visit_time')
    search_fields = ('ip_address', 'path')
    list_filter = ('ip_address', 'visit_time' )
