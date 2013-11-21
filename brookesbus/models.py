from django.core.urlresolvers import reverse
from django.db import models


class Bus(models.Model):
    name = models.CharField(max_length=255)
    stops = models.ManyToManyField('Stop')

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bus-detail', kwargs={'pk': self.pk})


class Stop(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stop-detail', kwargs={'pk': self.pk})


class Schedule(models.Model):
    bus = models.ForeignKey('Bus', related_name='bus')
    stop = models.ForeignKey('Stop', related_name='stops')
    eta = models.TimeField()
    route = models.ForeignKey('Route', related_name='route')

    class Meta:
        ordering = ['eta']


class Route(models.Model):
    name = models.CharField(max_length=255)
    start_time = models.TimeField()

    def __unicode__(self):
        name = self.name + ' ' + self.start_time.strftime('%I:%M%p')
        return name
