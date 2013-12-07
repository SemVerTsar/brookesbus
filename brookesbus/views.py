import datetime

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView

from .models import Bus, Stop, Schedule


class UpdateView(TemplateView):
    template_name = 'brookesbus/updates.html'


class TwitterView(TemplateView):
    template_name = 'brookesbus/twitter.html'


class FacebookView(TemplateView):
    template_name = 'brookesbus/facebook.html'


class AnimationView(TemplateView):
    template_name = 'brookesbus/animation.html'


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


class StopDetail(ListView):
    model = Schedule
    template_name = 'brookesbus/stop_detail.html'

    def get(self, request, *args, **kwargs):
        self.stop = get_object_or_404(Stop, pk=kwargs['pk'])
        return super(StopDetail, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super(StopDetail, self).get_context_data(stop=self.stop, **kwargs)

    def get_queryset(self):
        now = datetime.datetime.now()
        return self.stop.schedule.filter(eta__gte=now)
