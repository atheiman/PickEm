from django.db.models import Q
from pickem_app.models import *
import json, datetime, string
from pickem_app.global_vars import *

print "Deleting all objects in db."

Pick.objects.all().delete()
Game.objects.all().delete()
Team.objects.all().delete()
User.objects.all().delete()

print "Done."



print
print
print "Adding users."

superuser = User.objects.create_user(
	username='atheiman',
	first_name='Austin',
	last_name='Heiman',
	email='atheimanksu@gmail.com',
)
superuser.set_password('atheimanpass')
superuser.is_superuser = True
superuser.is_staff = True
superuser.save()

user = User.objects.create_user(
	username='johndoe',
	first_name='John',
	last_name='Doe',
	email='john.doe@gmail.com',
)
user.set_password('johnpass')
user.save()

user = User.objects.create_user(
	username='janedoe',
	first_name='Jane',
	last_name='Doe',
	email='jane.doe@gmail.com',
)
user.set_password('janepass')
user.save()

print "Users added:"

print User.objects.all()



print
print
print "Adding teams."

Team(abbreviation='NE', location='New England', nickname='Patriots').save()
Team(abbreviation='NYJ', location='New York', nickname='Jets').save()
Team(abbreviation='MIA', location='Miami', nickname='Dolphins').save()
Team(abbreviation='BUF', location='Buffalo', nickname='Bills').save()
Team(abbreviation='PIT', location='Pittsburgh', nickname='Steelers').save()
Team(abbreviation='BAL', location='Baltimore', nickname='Ravens').save()
Team(abbreviation='CLE', location='Cleveland', nickname='Browns').save()
Team(abbreviation='CIN', location='Cincinnati', nickname='Bengals').save()
Team(abbreviation='HOU', location='Houston', nickname='Texans').save()
Team(abbreviation='IND', location='Indianapolis', nickname='Colts').save()
Team(abbreviation='JAX', location='Jacksonville', nickname='Jaguars').save()
Team(abbreviation='TEN', location='Tennessee', nickname='Titans').save()
Team(abbreviation='DEN', location='Denver', nickname='Broncos').save()
Team(abbreviation='KC', location='Kansas City', nickname='Chiefs').save()
Team(abbreviation='SD', location='San Diego', nickname='Chargers').save()
Team(abbreviation='OAK', location='Oakland', nickname='Raiders').save()
Team(abbreviation='DAL', location='Dallas', nickname='Cowboys').save()
Team(abbreviation='WAS', location='Washington', nickname='Redskins').save()
Team(abbreviation='NYG', location='New York', nickname='Giants').save()
Team(abbreviation='PHI', location='Philadelphia', nickname='Eagles').save()
Team(abbreviation='MIN', location='Minnesota', nickname='Vikings').save()
Team(abbreviation='GB', location='Green Bay', nickname='Packers').save()
Team(abbreviation='DET', location='Detroit', nickname='Lions').save()
Team(abbreviation='CHI', location='Chicago', nickname='Bears').save()
Team(abbreviation='NO', location='New Orleans', nickname='Saints').save()
Team(abbreviation='TB', location='Tampa Bay', nickname='Buccaneers').save()
Team(abbreviation='ATL', location='Atlanta', nickname='Falcons').save()
Team(abbreviation='CAR', location='Carolina', nickname='Panthers').save()
Team(abbreviation='SF', location='San Francisco', nickname='49ers').save()
Team(abbreviation='SEA', location='Seattle', nickname='Seahawks').save()
Team(abbreviation='ARI', location='Arizona', nickname='Cardinals').save()
Team(abbreviation='STL', location='St. Louis', nickname='Rams').save()

print "Teams added:"

print Team.objects.all()



NFL_GAMES_JSON_LOCATION = 'other/nfl_games.json'

print
print
print "Adding games. Reading in '%s'." % NFL_GAMES_JSON_LOCATION

class jsonGame(object):
	def __init__(self, week_number, date, time, timezone, home_team, away_team):
		self.week_number = week_number
		self.date = date
		self.time = time
		self.timezone = timezone
		self.home_team = home_team
		self.away_team = away_team

def game_decoder(obj):
	return jsonGame(
		obj['week_number'],
		obj['date'],
		obj['time'],
		obj['timezone'],
		obj['home_team'],
		obj['away_team'],
	)

json_file = open(NFL_GAMES_JSON_LOCATION, 'r')

json_data = json_file.read()

games = json.loads(json_data, object_hook=game_decoder)

json_file.close()

# create date_time field from JSON date and time fields combined as string
# datetime.strptime(date_string, format)
# {"home_team":"DAL","away_team":"SF","week_number":"1","time":"4:25PM ","date":"Sunday, September 07","timezone":"ET"}
# "4:25PM Sunday, September 07 2014"
# %l	hour ( 1..12)
# %I	Hour (12-hour clock) as a zero-padded decimal number.	01, 02, ..., 12	
# %M	minute (00..59)
# %p	locale's equivalent of either AM or PM; blank if not known
# %A	locale's full weekday name (e.g., Sunday)
# %B	locale's full month name (e.g., January)
# %d	day of month (e.g, 01)
# %Y	Year with century as a decimal number.	1970, 1988, 2001, 2013
# %Z	Time zone name (empty string if the object is naive).	(empty), UTC, EST, CST

format = "%I:%M%p %A, %B %d %Y"

# >>> format = "%I:%M%p %A, %B %d %Y"
# >>> date_time = datetime.datetime.strptime("12:25PM Sunday, September 07 2014", format)
# >>> print date_time.strftime("%c")
# Sun Sep  7 12:25:00 2014

for g in games:
	date_time = "%s%s 2014" % (g.time, g.date)
	# if hour is only one digit
	if not date_time[1].isdigit():
		# append 0 to hour
		date_time = '0%s' % date_time
	
	# make datetime object
	date_time = datetime.datetime.strptime(date_time, format)
	date_time.time
	# print date_time.strftime("%c")
	
	Game(
		away_team=Team.objects.get(abbreviation=g.away_team),
		home_team=Team.objects.get(abbreviation=g.home_team),
		week=g.week_number,
		date_time=date_time,
	).save()

print "Games added:"

print Game.objects.all()



print
print
print "Adding winners to week 1 and week 2."

"""
>>> import nflgame
>>> games = nflgame.games(2014, week=1)
>>> g = games[0]
>>> g
<nflgame.game.Game object at 0x10c837990>
>>> str(g.home)
'SEA'
>>> str(g.away)
'GB'
>>> g.score_home
36
>>> g.score_away
16
>>> g.game_over()
True
>>> g.playing()
False
>>> g.nice_score()
u'GB (16) at SEA (36)'
>>> g.season()
2014
>>> g.time
<nflgame.game.GameClock object at 0x10c837a90>
>>> g.time.clock
u'00:21'
>>> g.time.quarter
9223372036854775807
>>> g.time.is_final()
True
>>> g.time.is_halftime()
False
>>> g.time.is_pregame()
False

games = nflgame.games(2014, week=3)
for g in games:
  print MULTILINECOMMENT
  {
    'week': 1,
    'home_team_abbreviation': '%s',
    'away_team_abbreviation': '%s',
    'spread': 0,
    'away_score': %i,
    'home_score': %i,
    'winner_abbreviation': '%s',
    'status': 'NOT_YET_STARTED',
  },ENDMULTILINECOMMENT % (g.home, g.away, g.score_away, g.score_home, g.winner)

"""



games = [
	{
		'week': 1,
		'home_team_abbreviation': 'SEA',
		'away_team_abbreviation': 'GB',
		'spread': -5.5,
		'away_score': 16,
		'home_score': 36,
		# 'winner_abbreviation': 'SEA',
		'status': 'COMPLETE',
	},
	{
		'week': 1,
		'home_team_abbreviation': 'ATL',
		'away_team_abbreviation': 'NO',
		'spread': -1.5,
		'away_score': 34,
		'home_score': 37,
		# 'winner_abbreviation': 'ATL',
		'status': 'COMPLETE',
	},
	{
		'week': 1,
		'home_team_abbreviation': 'BAL',
		'away_team_abbreviation': 'CIN',
		'spread': -2.5,
		'away_score': 23,
		'home_score': 16,
		# 'winner_abbreviation': 'CIN',
		'status': 'COMPLETE',
	},
	{
		'week': 1,
		'home_team_abbreviation': 'CHI',
		'away_team_abbreviation': 'BUF',
		'spread': -6.5,
		'away_score': 23,
		'home_score': 20,
		# 'winner_abbreviation': 'BUF',
		'status': 'COMPLETE',
	},
	{
		'week': 1,
		'home_team_abbreviation': 'HOU',
		'away_team_abbreviation': 'WAS',
		'spread': -2.5,
		'away_score': 6,
		'home_score': 17,
		# 'winner_abbreviation': 'HOU',
		'status': 'COMPLETE',
	},
	{
		'week': 1,
		'home_team_abbreviation': 'KC',
		'away_team_abbreviation': 'TEN',
		'spread': -6.5,
		'away_score': 26,
		'home_score': 10,
		# 'winner_abbreviation': 'TEN',
		'status': 'COMPLETE',
	},
	{
		'week': 1,
		'home_team_abbreviation': 'MIA',
		'away_team_abbreviation': 'NE',
		'spread': 3.5,
		'away_score': 20,
		'home_score': 33,
		# 'winner_abbreviation': 'MIA',
		'status': 'COMPLETE',
	},
	{
		'week': 1,
		'home_team_abbreviation': 'NYJ',
		'away_team_abbreviation': 'OAK',
		'spread': -4.5,
		'away_score': 14,
		'home_score': 19,
		# 'winner_abbreviation': 'NYJ',
		'status': 'COMPLETE',
	},
	{
		'week': 1,
		'home_team_abbreviation': 'PHI',
		'away_team_abbreviation': 'JAC',
		'spread': -11.5,
		'away_score': 17,
		'home_score': 34,
		# 'winner_abbreviation': 'PHI',
		'status': 'COMPLETE',
	},
	{
		'week': 1,
		'home_team_abbreviation': 'PIT',
		'away_team_abbreviation': 'CLE',
		'spread': -5.5,
		'away_score': 27,
		'home_score': 30,
		# 'winner_abbreviation': 'PIT',
		'status': 'COMPLETE',
	},
	{
		'week': 1,
		'home_team_abbreviation': 'STL',
		'away_team_abbreviation': 'MIN',
		'spread': -6.5,
		'away_score': 34,
		'home_score': 6,
		# 'winner_abbreviation': 'MIN',
		'status': 'COMPLETE',
	},
	{
		'week': 1,
		'home_team_abbreviation': 'DAL',
		'away_team_abbreviation': 'SF',
		'spread': 4.5,
		'away_score': 28,
		'home_score': 17,
		# 'winner_abbreviation': 'SF',
		'status': 'COMPLETE',
	},
	{
		'week': 1,
		'home_team_abbreviation': 'TB',
		'away_team_abbreviation': 'CAR',
		'spread': 1.5,
		'away_score': 20,
		'home_score': 14,
		# 'winner_abbreviation': 'CAR',
		'status': 'COMPLETE',
	},
	{
		'week': 1,
		'home_team_abbreviation': 'DEN',
		'away_team_abbreviation': 'IND',
		'spread': -6.5,
		'away_score': 24,
		'home_score': 31,
		# 'winner_abbreviation': 'DEN',
		'status': 'COMPLETE',
	},
	{
		'week': 1,
		'home_team_abbreviation': 'DET',
		'away_team_abbreviation': 'NYG',
		'spread': -4.5,
		'away_score': 14,
		'home_score': 35,
		# 'winner_abbreviation': 'DET',
		'status': 'COMPLETE',
	},
	{
		'week': 1,
		'home_team_abbreviation': 'ARI',
		'away_team_abbreviation': 'SD',
		'spread': -3.5,
		'away_score': 17,
		'home_score': 18,
		# 'winner_abbreviation': 'ARI',
		'status': 'COMPLETE',
	},
	{
		'week': 2,
		'home_team_abbreviation': 'BAL',
		'away_team_abbreviation': 'PIT',
		'spread': -2.5,
		'away_score': 6,
		'home_score': 26,
		# 'winner_abbreviation': 'BAL',
		'status': 'COMPLETE',
	},

	{
		'week': 2,
		'home_team_abbreviation': 'BUF',
		'away_team_abbreviation': 'MIA',
		'spread': 0.5,
		'away_score': 10,
		'home_score': 29,
		# 'winner_abbreviation': 'BUF',
		'status': 'COMPLETE',
	},

	{
		'week': 2,
		'home_team_abbreviation': 'CAR',
		'away_team_abbreviation': 'DET',
		'spread': -2.5,
		'away_score': 7,
		'home_score': 24,
		# 'winner_abbreviation': 'CAR',
		'status': 'COMPLETE',
	},

	{
		'week': 2,
		'home_team_abbreviation': 'CIN',
		'away_team_abbreviation': 'ATL',
		'spread': -5.5,
		'away_score': 10,
		'home_score': 24,
		# 'winner_abbreviation': 'CIN',
		'status': 'COMPLETE',
	},

	{
		'week': 2,
		'home_team_abbreviation': 'CLE',
		'away_team_abbreviation': 'NO',
		'spread': 6.5,
		'away_score': 24,
		'home_score': 26,
		# 'winner_abbreviation': 'CLE',
		'status': 'COMPLETE',
	},

	{
		'week': 2,
		'home_team_abbreviation': 'MIN',
		'away_team_abbreviation': 'NE',
		'spread': 3.5,
		'away_score': 30,
		'home_score': 7,
		# 'winner_abbreviation': 'NE',
		'status': 'COMPLETE',
	},

	{
		'week': 2,
		'home_team_abbreviation': 'NYG',
		'away_team_abbreviation': 'ARI',
		'spread': -1.5,
		'away_score': 25,
		'home_score': 14,
		# 'winner_abbreviation': 'ARI',
		'status': 'COMPLETE',
	},

	{
		'week': 2,
		'home_team_abbreviation': 'TEN',
		'away_team_abbreviation': 'DAL',
		'spread': -3.5,
		'away_score': 26,
		'home_score': 10,
		# 'winner_abbreviation': 'DAL',
		'status': 'COMPLETE',
	},

	{
		'week': 2,
		'home_team_abbreviation': 'WAS',
		'away_team_abbreviation': 'JAC',
		'spread': -5.5,
		'away_score': 10,
		'home_score': 41,
		# 'winner_abbreviation': 'WAS',
		'status': 'COMPLETE',
	},

	{
		'week': 2,
		'home_team_abbreviation': 'SD',
		'away_team_abbreviation': 'SEA',
		'spread': 5.5,
		'away_score': 21,
		'home_score': 30,
		# 'winner_abbreviation': 'SD',
		'status': 'COMPLETE',
	},

	{
		'week': 2,
		'home_team_abbreviation': 'TB',
		'away_team_abbreviation': 'STL',
		'spread': -5.5,
		'away_score': 19,
		'home_score': 17,
		# 'winner_abbreviation': 'STL',
		'status': 'COMPLETE',
	},

	{
		'week': 2,
		'home_team_abbreviation': 'DEN',
		'away_team_abbreviation': 'KC',
		'spread': -13.5,
		'away_score': 17,
		'home_score': 24,
		# 'winner_abbreviation': 'DEN',
		'status': 'COMPLETE',
	},

	{
		'week': 2,
		'home_team_abbreviation': 'GB',
		'away_team_abbreviation': 'NYJ',
		'spread': -8.5,
		'away_score': 24,
		'home_score': 31,
		# 'winner_abbreviation': 'GB',
		'status': 'COMPLETE',
	},

	{
		'week': 2,
		'home_team_abbreviation': 'OAK',
		'away_team_abbreviation': 'HOU',
		'spread': 2.5,
		'away_score': 30,
		'home_score': 14,
		# 'winner_abbreviation': 'HOU',
		'status': 'COMPLETE',
	},

	{
		'week': 2,
		'home_team_abbreviation': 'SF',
		'away_team_abbreviation': 'CHI',
		'spread': -7.5,
		'away_score': 28,
		'home_score': 20,
		# 'winner_abbreviation': 'CHI',
		'status': 'COMPLETE',
	},

	{
		'week': 2,
		'home_team_abbreviation': 'IND',
		'away_team_abbreviation': 'PHI',
		'spread': -2.5,
		'away_score': 30,
		'home_score': 27,
		# 'winner_abbreviation': 'PHI',
		'status': 'COMPLETE',
	},
]



for g in games:
	game = Game.objects.get(week=g['week'], home_team=Team.objects.get(abbreviation=g['home_team_abbreviation']))
	game.spread = g['spread']
	game.away_score = g['away_score']
	game.home_score = g['home_score']
	game.status = g['status']
	game.save()

print "games set."

# games = Game.objects.filter(Q(week=1) | Q(week=2))
# for game in games:
# 	if game.winner is None:
# 		print "NO WINNER FOR THESE: %r" % game
# 	else:
# 		print game.winner.abbreviation



print
print
print "Setting straight up and against the spread winners for all games."
# set game winners and spread winners
execfile('other/set_winners.py')



print
print
print "Creating a couple test picksets for each user."
# create two picksets for each user
users = [
	User.objects.get(username='johndoe'),
	User.objects.get(username='janedoe'),
]
weeks = [1, 2]
for user in users:
	for week in weeks:
		pickset = Pickset(user=user, week=week)
		pickset.save()



print
print
print "Dropping a few test picks in each pickset."
# put a few picks in each pickset
picksets = Pickset.objects.all()
for pickset in picksets:
	games = Game.objects.filter(week=pickset.week)
	for game in games:
		if (game.id + pickset.user.id) % 3 == 0:  # pick a random third of the games
			if (game.id + pickset.user.id) % 2 == 0:  # pick either home or away randomly
				pick = HOME
			else:
				pick = AWAY
			p = Pick(pickset=pickset, game=game, pick=pick)
			p.save()



print
print
print "Scoring the picksets."
# set Pickset.attempts and Pickset.correct
execfile('other/score_picksets.py')



print
print
print "Opening up week 3 for picks"

games = Game.objects.filter(week=3)
for g in games:
	g.status = NOT_YET_STARTED
	g.save()

print "Week 3 games set to NOT_YET_STARTED. No spreads yet set for these games though."