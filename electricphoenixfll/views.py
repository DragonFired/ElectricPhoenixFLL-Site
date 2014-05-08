from django.shortcuts import render
from phoenixFollowers.models import Contact
from phoenixMembers.models import TeamMember
from phoenixEvents.models import Event
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils.safestring import mark_safe
from phoenixEvents.models import EventCalendar

def home(request):
	return render(request, 'index.html', {})

def calendar(request):
	return render(request, 'calendar.html', {})

def forum(request):
	return render(request, 'forum.html', {})

def donate(request):
	return render(request, 'donate.html', {})

def donate_thanks(request):
	return render(request, 'donate_thanks.html', {})

def what_is_fll(request):
	return render(request, 'what_is_fll.html', {})

def core_values(request):
	return render(request, 'core_values.html', {})

def follow_the_phoenix(request):
	return render(request, 'follow.html', {})

def followEnter(request):
	if 'first_name' in request.POST and 'last_name' in request.POST and 'email' in request.POST:
		newFirstName = request.POST['first_name']
		newLastName = request.POST['last_name']
		newEmail = request.POST['email']
		newCity = ""
		if 'city' in request.POST:
			newCity = request.POST['city']
		newStateProvince = ""
		if 'stateProvince' in request.POST:
			newStateProvince = request.POST['stateProvince']
		newCountry = ""
		if 'country' in request.POST:
			newCountry = request.POST['country']
		newContact = Contact(firstName = newFirstName, lastName = newLastName, email = newEmail, city = newCity, stateProvince = newStateProvince, country = newCountry)
		newContact.save()
	else:
		message = 'You submitted an empty form.'
		return HttpResponse(message)
	return render(request, 'follow_thanks.html', {'firstName': newFirstName})

def followList(request):
	contactList = Contact.objects.all().order_by('firstName')
	return render(request, 'follow_list.html', {'contactList': contactList})

def about_us(request):
	membersList = TeamMember.objects.all().order_by('-role', 'firstName')
	return render(request, 'about_us.html', {'membersList': membersList})

# def testcalendar(request, year, month):
# 	myEvents = Event.objects.order_by('eventDate').filter(eventDate__year=year, eventDate__month=month,)
# 	cal = EventCalendar(myEvents).formatmonth(year, month)
# 	return render_to_response('test_calendar.html', {'calendar': mark_safe(cal),})

def testcalendar(request, year, month):
	myEvents = Event.objects.order_by('eventDate').filter(eventDate__year=year, eventDate__month=month,)
	screenCalendar = EventCalendar(myEvents).formatmonth(year, month)
	topEventsList = Event.objects.all().order_by('eventDate')[:3]
	return render_to_response('test_calendar.html', {'calendar': mark_safe(screenCalendar),'topEvents': topEventsList,})


# 	db = MySQLdb.connect(user='arana', db='bookdb', password='secret', host='localhost')
# 	cursor = db.cursor()
# 	cursor.execute('SELECT anme FROM books ORDER BY name')
# 	names = [row[0] for row in cursor.fetchall()]
# 	db.close()
# 	return render(request, 'bookList.html', {'names': names})
