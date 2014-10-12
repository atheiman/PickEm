from pickem_app.models import *

# Get all picksets
picksets = Pickset.objects.all()

for ps in picksets:
	ps.attempts = ps.picks.all().count()
	ps.correct = 0
	for p in ps.picks.all():
		# increment correct for correct picks, decrement for missed picks
		if p.is_correct():
			ps.correct += 1
		else:
			ps.correct -= 1
	ps.save()
