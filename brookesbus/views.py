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

    def get_context_data(self, **kwargs):
        kwargs['timenow'] = datetime.datetime.now().time()
        return super(StopDetail, self).get_context_data(**kwargs)

    # def get_queryset(self):
    #     now = datetime.datetime.now().time()
    #     qs = super(StopDetail, self).get_queryset()
    #     return qs.filter(schedule__eta__gte=now)
