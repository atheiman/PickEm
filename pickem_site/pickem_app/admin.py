from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from pickem_app.models import *
from pickem_app.global_vars import *

admin.site.site_header = "PickEm Administration"
admin.site.site_title = "PickEm Adminstration"
admin.site.index_title = "PickEm Administration Home"



# def make_published(modeladmin, request, queryset):
#     queryset.update(status='p')
# make_published.short_description = "Mark selected stories as published"

# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ['title', 'status']
#     ordering = ['title']
#     actions = [make_published]

# admin.site.register(Article, ArticleAdmin)



class TeamAdmin(admin.ModelAdmin):
	fields = ['abbreviation', 'location', 'nickname']
	list_display = ['id', 'abbreviation', 'location', 'nickname']
	# search_fields = ['abbreviation', 'location', 'nickname']



def make_in_progress(modeladmin, request, queryset):
	queryset.update(status=IN_PROGRESS)
make_in_progress.short_description = "Mark selected games as In Progress"



def make_not_yet_started(modeladmin, request, queryset):
	queryset.update(status=NOT_YET_STARTED)
make_not_yet_started.short_description = "Mark selected games as Not Yet Started"



def make_complete(modeladmin, request, queryset):
	queryset.update(status=COMPLETE)
make_complete.short_description = "Mark selected games as Complete"



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
	]
	list_display = [
		'id',
		'week',
		'away_team',
		'home_team',
		'status',
		'date_time',
		'spread',
		'spread_winner',
	]
	list_filter = ['week',]
	ordering = ['date_time']
	actions = [make_in_progress, make_not_yet_started, make_complete]
	# search_fields = ['week', 'away_team', 'home_team']



# Register Admin pages
admin.site.register(Team, TeamAdmin)
admin.site.register(Game, GameAdmin)
