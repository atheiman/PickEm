from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .global_vars import *
from .models import *



# SELECT DISTINCT week from Game
# SELECT DISTINCT only supported on PostgreSQL, so make my own...
# weeks list holds all weeks that have a game
weeks = []
for w in range(1,22):
	count = Game.objects.filter(week=w).count()
	if count > 0:
		weeks.append(w)



def index(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('pickem_app:user',kwargs={'username':request.user.username}))
	context = {
		'page_title': "Home",
	}
	return render(request, 'pickem_app/index.html', context)



# List all the users signed up
def users_list(request):
	users = User.objects.all()
	context = {
		'users': users,
		'page_title': "All PickEm'sters",
	}
	return render(request, 'pickem_app/users_list.html', context)



# Show basic user information
def user(request, username):
	view_user = get_object_or_404(User, username=username)
	context = {
		'weeks': weeks,
		'view_user': view_user,
		'page_title': view_user.username,
	}
	return render(request, 'pickem_app/user.html', context)



# Show user's picks for a specified week
def pickset(request, username, week):
	view_user = get_object_or_404(User, username=username)
	
	if request.user == view_user:
		editable = True
	else:
		editable = False
	
	# If no pickset yet for this week and this user, create a new one.
	try:
		pickset = Pickset.objects.get(week=week, user=view_user)
	except Pickset.DoesNotExist:
		pickset = Pickset(user=view_user, week=week)
		pickset.save()
	
	pickset.set_attempts_and_correct()
	
	games = get_list_or_404(Game.objects.filter(week=week).order_by("date_time"))
	
	page_title = "<a href='/u/%s'>%s</a>'s Week %s Picks" % (view_user.username, view_user.username, week)
	context = {
		'pickset': pickset,
		'view_user': view_user,
		'week': week,
		'page_title': page_title,
		'weeks': weeks,
		'games': games,
		'editable': editable,
		
		'AGAINST_THE_SPREAD': AGAINST_THE_SPREAD,
		'STRAIGHT_UP': STRAIGHT_UP,
		'HOME': HOME,
		'AWAY': AWAY,
		'NOT_YET_STARTED': NOT_YET_STARTED,
		'IN_PROGRESS': IN_PROGRESS,
		'COMPLETE': COMPLETE,
		'OTHER_AVAILABLE': OTHER_AVAILABLE,
		'OTHER_UNAVAILABLE': OTHER_UNAVAILABLE,
	}
	return render(request, 'pickem_app/pickset.html', context)



# How to dump all POST elements
# return_string = '<p>POST Elements:<br>'
# for key, value in request.POST.iteritems():   # iter on both keys and values
# 	return_string += "%s:%s<br>" % (key, value)
# return_string == '</p>'
# return HttpResponse(return_string)



# POST api for editing a pickset
def api_pickset(request, pickset_id):
	pickset = get_object_or_404(Pickset, id=pickset_id)
	username = pickset.user.username
	user = User.objects.get(username=username)
	week = pickset.week
	
	# TODO check username of session matches the username of the pickset or fail
	
	games_already_picked = []
	for p in pickset.picks.all():
		games_already_picked.append(p.game)
	
	# submit the picks to the DB
	for key, value in request.POST.iteritems():
		if key.startswith('game'):
			game = Game.objects.get(id=key.strip('game'))
			
			if game in games_already_picked:
				# UPDATE the pick if previously picked
				p = Pick.objects.get(pickset=pickset, game=game)
				p.pick = value
			else:
				# INSERT the pick if not yet picked
				p = Pick(pickset=pickset, game=game, pick=value)
				# append game to ensure only one pick per game per pickset
				games_already_picked.append(game)
			p.save()
	
	return HttpResponseRedirect(reverse('pickem_app:pickset', args=(user.username, week)))


