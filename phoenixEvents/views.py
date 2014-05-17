from django.shortcuts import render_to_response
from django.utils.safestring import mark_safe
from phoenixEvents.models import EventCalendar
from phoenixEvents.models import Event
import datetime

# Create your views here.

def calendarDetail(request, slug=None, year = 0, month = 0):
	if year == 0:
		now = datetime.datetime.now()
		year = now.year
		month = now.month
	myEvents = Event.objects.order_by('eventDate').filter(eventDate__year=year, eventDate__month=month,)
	screenCalendar = EventCalendar(myEvents).formatmonth(year, month)
	event = Event.objects.get(slug=slug)
	return render_to_response('calendarDetail.html', {'calendar': mark_safe(screenCalendar),'event': event,})
