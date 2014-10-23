from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.db.models import Q
import datetime

from global_vars import *



class Team(models.Model):
	abbreviation = models.CharField(max_length=5, unique=True)
	location = models.CharField(max_length=100)
	nickname = models.CharField(max_length=100)
	
	def return_record(self):
		games = (Game.objects.filter(home_team=self)|Game.objects.filter(away_team=self))
		games_played_count = games.exclude(~Q(status=COMPLETE)).count()
		wins = games.filter(winner=self).count()
		losses = games.exclude(winner=self).count() - games.filter(winner__isnull=True).count()
		# Check for ties
		ties = games_played_count - wins - losses
		if ties != 0:
			return "(%i - %i - %i)" % (wins, losses, ties)
		else:
			return "(%i - %i)" % (wins, losses)
	
	def __unicode__(self):
		# return "team_id:%i, abbreviation:%s" % (self.id, self.abbreviation)
		return self.abbreviation



class Game(models.Model):
	away_team = models.ForeignKey(Team, related_name='away_games')
	away_score = models.PositiveIntegerField(blank=True, null=True)
	home_team = models.ForeignKey(Team, related_name='home_games')
	home_score = models.PositiveIntegerField(blank=True, null=True)
	week = models.PositiveIntegerField(validators=[MaxValueValidator(22)])
	spread = models.FloatField(default=0)
	winner = models.ForeignKey(Team, related_name='games_won_su', blank=True, null=True)
	spread_winner = models.ForeignKey(Team, related_name='games_won_ats', blank=True, null=True)
	STATUS_CHOICES = (
		(NOT_YET_STARTED, "Not yet started"),
		(IN_PROGRESS, "In progress"),
		(COMPLETE, "Complete"),
		(OTHER_AVAILABLE, "Other - available"),
		(OTHER_UNAVAILABLE, "Other - unavailable"),
	)
	status = models.CharField(
		max_length=30,
		choices=STATUS_CHOICES,
		default=OTHER_UNAVAILABLE,
	)
	date_time = models.DateTimeField(blank=True, null=True)
	
	def weekday(self):
		return self.date_time.strftime("%a")
	
	def short_date(self):
		return self.date_time.strftime("%a %b %d")
	
	def time(self):
		return_string = self.date_time.strftime("%I:%M %p EST")
		if return_string[0] == '0':
			return_string = return_string[1:]
		return return_string
		
	def save(self, *args, **kwargs):
		if self.status == COMPLETE:
			# set winner
			if self.home_score is None or self.away_score is None:
				self.winner = None
			elif self.home_score > self.away_score:
				self.winner = self.home_team
			elif self.home_score < self.away_score:
				self.winner = self.away_team
			else:
				self.winner = None
			# set spread_winner
			if self.home_score is None or self.away_score is None:
				self.spread_winner = None
			elif self.home_score + self.spread > self.away_score:
				self.spread_winner = self.home_team
			elif self.home_score + self.spread < self.away_score:
				self.spread_winner = self.away_team
			else:
				self.spread_winner = None
		
		# save
		super(Game, self).save(*args, **kwargs)
	
	# Get all Chiefs home games:
	# Game.objects.filter(home_team=Team.objects.get(abbreviation='KC'))
	
	def __unicode__(self):
		return "game_id: %i, %s@%s, wk: %i" % (self.id, self.away_team, self.home_team, self.week)



class Pickset(models.Model):
	user = models.ForeignKey(User, related_name='picksets')
	week = models.PositiveIntegerField(validators=[MaxValueValidator(22)])
	attempts = models.PositiveIntegerField(validators=[MaxValueValidator(16)], blank=True, null=True)
	score = models.IntegerField(validators=[MaxValueValidator(16), MinValueValidator(-16)], blank=True, null=True)
	
	GAMETYPE_CHOICES = (
		(STRAIGHT_UP, "straight-up"),
		(AGAINST_THE_SPREAD, "against the spread"),
	)
	gametype = models.CharField(
		max_length=19,
		choices=GAMETYPE_CHOICES,
		default='ATS'
	)
	
	def set_attempts_and_score(self):
		self.attempts = self.picks.all().count()
		self.score = 0
		for p in self.picks.all():
			# increment score for score picks, decrement for missed picks
			if p.game == COMPLETE:
				if p.is_correct():
					self.score += 1
				else:
					self.score -= 1
		self.save()
	
	def __unicode__(self):
		return "pickset_id %i, user %s, week %i" % (self.id, self.user, self.week)



class Pick(models.Model):
	pickset = models.ForeignKey(Pickset, related_name='picks')
	game = models.ForeignKey(Game, related_name='picks')
	PICK_CHOICES = (
		(HOME, "home"),
		(AWAY, "away"),
	)
	pick = models.CharField(
		max_length=4,
		choices=PICK_CHOICES,
	)
	
	def team_picked(self):
		return Team.objects.get(abbreviation=self.abbreviation)
	
	def abbreviation(self):
		game = Game.objects.get(id=self.game_id)
		if self.pick == HOME:
			return Game.objects.get(id=self.game_id).home_team.abbreviation
		elif self.pick == AWAY:
			return Game.objects.get(id=self.game_id).away_team.abbreviation
		else:
			return "ERROR: Pick not logged as %s or %s" % (AWAY, HOME)
	
	def is_correct(self):
		if self.game.spread_winner is None:
			pass
		if self.team_picked() == self.game.spread_winner:
			return True
		else:
			return False
	
	def __unicode__(self):
		return "pick_id: %i, pickset: %s, game: %s, pick: %s, abbreviation: %s" % (self.id, self.pickset, self.game, self.pick, self.abbreviation())
	
	# get a specific pick
	# Pick.objects.filter(pickset=Pickset.objects.get(user=User.objects.get(username='johndoe'),week=9),game=Game.objects.get(home_team=Team.objects.get(abbreviation='HOU'), week=9),)


