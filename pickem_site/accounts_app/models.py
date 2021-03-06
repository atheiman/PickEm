from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class NflPickemProfile(models.Model):
	# reference the django user
	user = models.OneToOneField(User, related_name='NflPickemProfile')
	
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
	
	def __unicode__(self):
		# return "team_id:%i, abbreviation:%s" % (self.id, self.abbreviation)
		return self.user.username



def create_user_profile(sender, instance, created, **kwargs):
	if created:
		NflPickemProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
