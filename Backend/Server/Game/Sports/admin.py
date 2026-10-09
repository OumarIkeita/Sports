from django.contrib import admin
from .models import Club, Athlete,Competition, Team,TeamStaff,TournamentStanding,Match,MatchParticipant,PerformanceMetric,Injury
# Register your models here.
admin.site.register(Club)
admin.site.register(Competition)
admin.site.register(Team)
admin.site.register(TournamentStanding)
admin.site.register(TeamStaff)
admin.site.register(MatchParticipant)
admin.site.register(Match)
admin.site.register(PerformanceMetric)
admin.site.register(Injury)
admin.site.register(Athlete)