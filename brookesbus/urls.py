from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin

from . import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include(patterns('',
        url(r'^$', views.BusList.as_view(), name='bus-list'),
        ))),
    url(r'^bus/', include(patterns('',
        url(r'^(?P<pk>\d+)/', views.BusDetail.as_view(), name='bus-detail'),
        ))),
    url(r'^schedule/', include(patterns('',
        url(r'^(?P<pk>\d+)/', views.ScheduleDetail.as_view(), name='schedule-detail'),
        ))),
    url(r'^stop/', include(patterns('',
        url(r'^(?P<pk>\d+)/', views.StopDetail.as_view(), name='stop-detail'),
        ))),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

