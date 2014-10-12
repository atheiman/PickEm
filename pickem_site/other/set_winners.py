import sys

from pickem_app.models import *

games = Game.objects.all()

for g in games:
	# set straight up winner
	if g.home_score is not None and g.away_score is not None:
		if g.home_score > g.away_score:
			g.winner = g.home_team
		else:
			g.winner = g.away_team
		
		# set spread winner
		if g.home_score + g.spread > g.away_score:
			g.spread_winner = g.home_team
		else:
			g.spread_winner = g.away_team
	
	# save
	g.save()