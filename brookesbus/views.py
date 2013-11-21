from django.views.generic import DetailView, ListView

from .models import Bus, Stop, Schedule


class BusList(ListView):
    model = Bus
    template_name = 'brookesbus/bus_list.html'


class BusDetail(DetailView):
    model = Bus
