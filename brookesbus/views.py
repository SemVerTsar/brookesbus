from django.views.generic import DetailView, ListView, TemplateView

import datetime

from .models import Bus, Stop, Schedule


class UpdateView(TemplateView):
    template_name = 'brookesbus/updates.html'


class TwitterView(TemplateView):
    template_name = 'brookesbus/twitter.html'


class FacebookView(TemplateView):
    template_name = 'brookesbus/facebook.html'


class AnimationView(TemplateView):
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
        timenow = datetime.datetime.now().time()
        kwargs['schedule_list'] = self.object.schedule.all().filter(eta__gte=timenow)
        return super(StopDetail, self).get_context_data(**kwargs)
