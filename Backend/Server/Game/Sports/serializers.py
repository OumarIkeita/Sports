from rest_framework import serializers
from .models import (
    Club, Team, Athlete, Staff, TeamStaff, 
    Competition, Match, MatchParticipant, 
    PerformanceMetric, TournamentStanding
)

#----------------------Club serializer------------------------
class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields ='__all__'

#----------------------Competition serializer------------------------
class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = '__all__'

#----------------------Athlete serializer------------------------
class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields ='__all__'
#----------------------Staff serializer------------------------
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields ='__all__'
#----------------------TeamStaff serializer------------------------
class TeamStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamStaff
        fields ='__all__'

#----------------------Team serializer------------------------
class TeamSerializer(serializers.ModelSerializer):
    # Allows fetching all athletes belonging to this team at once
    athletes = AthleteSerializer(many=True, read_only=True)
    club_name = serializers.CharField(source='club.name', read_only=True)

    class Meta:
        model = Team
        fields = '__all__'

#----------------------MatchParticipant serializer------------------------
class MatchParticipantSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source='team.team_name', read_only=True)

    class Meta:
        model = MatchParticipant
        fields = '__all__'

#----------------------Match serializer------------------------
class MatchSerializer(serializers.ModelSerializer):
    # Generates a clean nested view of the participating teams and their metrics
    participants = MatchParticipantSerializer(source='matchparticipant_set', many=True, read_only=True)
    competition_name = serializers.CharField(source='competition.name', read_only=True)

    class Meta:
        model = Match
        fields = '__all__'


#----------------------PerformanceMetric serializer------------------------
class PerformanceMetricSerializer(serializers.ModelSerializer):
    athlete_display = serializers.CharField(source='athlete.__str__', read_only=True)

    class Meta:
        model = PerformanceMetric
        fields = '__all__'

#----------------------TournamentStanding serializer------------------------
class TournamentStandingSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source='team.team_name', read_only=True)
    point_differential = serializers.IntegerField(read_only=True) # Exposes the model property

    class Meta:
        model = TournamentStanding
        fields = '__all__'

#----------------------ClubDashboard serializer------------------------
class ClubDashboardSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(many=True, read_only=True)
    staff = StaffSerializer(many=True, read_only=True)

    class Meta:
        model = Club
        fields = [
            'club_id', 'name', 'short_name', 'foundation_year', 
            'headquarters_address', 'contact_email', 'contact_phone', 
            'teams', 'staff'
        ]