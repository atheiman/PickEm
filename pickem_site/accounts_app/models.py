from django.db import models
from django.contrib.auth.models import User

class NflPickemProfile(models.Model):
	# reference the django user
	user = models.OneToOneField(User)
	
	season_score = models.IntegerField(blank=True, null=True)
	season_attempts = models.IntegerField(blank=True, null=True)
	
	def set_season_score_and_attempts(self):
		picksets = self.user.picksets.all()
		season_score = season_attempts = 0
		
		for ps in picksets:
			ps.set_attempts_and_score()
			season_score += ps.score
			season_attempts += ps.attempts
		
		self.season_score = season_score
		self.season_attempts = season_attempts
		self.save()
