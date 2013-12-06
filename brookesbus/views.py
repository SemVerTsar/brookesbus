from django.views.generic import DetailView, ListView, TemplateView

import datetime

from .models import Bus, Stop, Schedule


class UpdateView(TemplateView):
    template_name = 'brookesbus/updates.html'


class TwitterView(TemplateView):
    template_name = 'brookesbus/twitter.html'


class FacebookView(TemplateView):
    template_name = 'brookesbus/facebook.html'


class AnnimationView(TemplateView):
    template_name = 'brookesbus/annimation.html'


class HomeView(TemplateView):
    template_name = 'brookesbus/home.html'


class BusList(ListView):
    model = Bus


class BusDetail(DetailView):
    model = Bus


class ScheduleDetail(DetailView):
    model = Schedule


class StopList(ListView):
    model = Stop


class StopDetail(DetailView):
    model = Stop

    def get_context_data(self, **kwargs):
        now = datetime.datetime.now()
        delta = datetime.timedelta(hours=2)
        kwargs['timenow'] = now.time()
        delta = now + delta
        kwargs['deltatime'] = delta.time()
        return super(StopDetail, self).get_context_data(**kwargs)
