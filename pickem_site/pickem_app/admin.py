from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from pickem_app.models import *

admin.site.site_header = "PickEm Administration"
admin.site.site_title = "PickEm Adminstration"
admin.site.index_title = "PickEm Administration Home"



# class PickerInline(admin.StackedInline):
# 	model = Picker
# 	can_delete = False
# 	verbose_name_plural = 'picker'



# class UserAdmin(admin.ModelAdmin):
# 	inlines = (PickerInline, )



class TeamAdmin(admin.ModelAdmin):
	fields = ['abbreviation', 'location', 'nickname']
	list_display = ['id', 'abbreviation', 'location', 'nickname']
	# search_fields = ['abbreviation', 'location', 'nickname']



class GameAdmin(admin.ModelAdmin):
	fields = [
		'away_team',
		'home_team',
		'status',
		'week',
		'date_time',
		'spread',
		'away_score',
		'home_score',
		'winner',
		'spread_winner',
	]
	list_display = ['id', 'week', 'away_team', 'home_team', 'status', 'date_time', 'spread', 'spread_winner']
	list_filter = ['week',]
	ordering = ['date_time']
	# search_fields = ['week', 'away_team', 'home_team']



# Register Admin pages
admin.site.register(Team, TeamAdmin)
admin.site.register(Game, GameAdmin)
