from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'electricphoenixfll.views.home', name='home'),
    url(r'^home$', 'electricphoenixfll.views.home', name='home'),
    url(r'^calendar$', 'electricphoenixfll.views.calendar', name='calendar'),
    url(r'^calendar/(?P<year>\d{4})/(?P<month>\d{1,2})/$', 'electricphoenixfll.views.calendar', name='calendar'),
    url(r'^forum$', 'electricphoenixfll.views.forum', name='forum'),
    url(r'^donate$', 'electricphoenixfll.views.donate', name='donate'),
    url(r'^donate_thanks$', 'electricphoenixfll.views.donate_thanks', name='donate_thanks'),
    url(r'^what_is_fll$', 'electricphoenixfll.views.what_is_fll', name='what_is_fll'),
    url(r'^core_values$', 'electricphoenixfll.views.core_values', name='core_values'),
    url(r'^follow_the_phoenix$', 'electricphoenixfll.views.follow_the_phoenix', name='follow_the_phoenix'),
    url(r'^followEnter/$', 'electricphoenixfll.views.followEnter', name='followEnter'),
    url(r'^followList/$', 'electricphoenixfll.views.followList', name='followList'),
    url(r'^about_us$', 'electricphoenixfll.views.about_us', name='about_us'),
    url(r'^privacy$', 'electricphoenixfll.views.privacy', name='privacy'),
    url(r'^calendarDetail/(?P<slug>[\w-]+)/$', 'phoenixEvents.views.calendarDetail', name='pEventsCalendarDetail'),

    url(r'^admin/', include(admin.site.urls)),
)
