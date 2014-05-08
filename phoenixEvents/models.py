from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class Event(models.Model):
	eventName = models.CharField(max_length=40)
	eventDescription = models.TextField()
	eventDate = models.DateField()
	eventTime = models.TimeField()
	eventLocation = models.CharField(max_length=60, null=True, blank=True)
	creationDate = models.DateField(auto_now_add=True)
	eventURL = models.URLField(null=True, blank=True)

	def __str__(self):
		return self.eventName + self.eventDescription + str(self.eventDate) + self.eventLocation + str(self.creationDate) + self.eventURL

from calendar import HTMLCalendar
from datetime import date
from itertools import groupby

from django.utils.html import conditional_escape as esc

class EventCalendar(HTMLCalendar):

    def __init__(self, events, firstWeekDay = 6):
        super(EventCalendar, self).__init__()
        self.events = self.group_by_day(events)
        self.setfirstweekday(firstWeekDay)

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += ' today'
            if day in self.events:
                cssclass += ' filled'
                body = ['<ul>']
                for event in self.events[day]:
                    body.append('<li>')
                    body.append('<a href="%s">' % events.get_absolute_url())
                    body.append(escape(event.title))
                    body.append('</a></li>')
                body.append('</ul>')
                return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
            return self.day_cell(cssclass, day)
        return self.day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(EventCalendar, self).formatmonth(year, month)

    def group_by_day(self, events):
#         field = lambda event: event.eventDate.day
#         return dict([(day, list(items)) for day, items in groupby(events, field)],)
        return

#    def field(event):
#        return event.eventDate.day

    def day_cell(self, cssclass, body):
        return '<td class="%s">%s</td>' % (cssclass, body)