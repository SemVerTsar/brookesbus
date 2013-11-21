from django.contrib import admin
from brookesbus.models import Bus, Stop, Schedule


class BusAdmin(admin.ModelAdmin):
    list_display = ('name',)

    list_filter = ['stops', ]

admin.site.register(Bus, BusAdmin)


class StopAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Stop, StopAdmin)


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('bus', 'stop', 'eta')

admin.site.register(Schedule, ScheduleAdmin)
