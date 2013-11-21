from django.views.generic import DetailView, ListView

from .models import Bus, Stop, Schedule


class BusList(ListView):
    model = Bus


class BusDetail(DetailView):
    model = Bus


class ScheduleDetail(DetailView):
    model = Schedule


class StopDetail(DetailView):
    model = Stop
