from django.contrib import admin
from .models import Profile, Report


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'nickname', 'photo']


class ReportAdmin(admin.ModelAdmin):
    list_display = ['user', 'reported_user', 'report_datetime']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Report, ReportAdmin)

