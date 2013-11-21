from django.contrib import admin
from brookesbus.models import Bus, Stop, Route, Schedule


class BusAdmin(admin.ModelAdmin):
    list_display = ('name',)

    list_filter = ['stops', ]

admin.site.register(Bus, BusAdmin)


class StopAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Stop, StopAdmin)


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('bus', 'stop', 'eta', 'route')

admin.site.register(Schedule, ScheduleAdmin)


class RouteAdmin(admin.ModelAdmin):
    list_display = ('start_time',)


admin.site.register(Route, RouteAdmin)
