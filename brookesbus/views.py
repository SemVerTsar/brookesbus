from django.views.generic import DetailView, ListView

import datetime

from .models import Bus, Stop, Schedule


class BusList(ListView):
    model = Bus


class BusDetail(DetailView):
    model = Bus


class ScheduleDetail(DetailView):
    model = Schedule


class StopDetail(DetailView):
    model = Stop

    def get_queryset(self):
        time = datetime.time
        qs = super(StopDetail, self).get_queryset()
        return qs.filter(stops__eta >= time)
