from django.db import models

# Create your models here.

#Club Table
class Club(models.Model):
    club_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150)  # NOT NULL by default
    short_name = models.CharField(max_length=50, null=True, blank=True)
    foundation_year = models.IntegerField(null=True, blank=True)
    headquarters_address = models.CharField(max_length=255, null=True, blank=True)
    contact_email = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    contact_phone = models.CharField(max_length=30, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


#------------------------------------------------------------------------------------------
#Team Table
class Team(models.Model):
    GENDER_CATEGORIES = [
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Mixed', 'Mixed'),
    ]

    team_id = models.BigAutoField(primary_key=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='teams')
    team_name = models.CharField(max_length=100)
    gender_category = models.CharField(max_length=20, choices=GENDER_CATEGORIES, null=True, blank=True)
    age_group = models.CharField(max_length=50, default='Senior')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team_name

#-------------------------------------------------------------------------------
#Athlete Table
class Athlete(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Injured', 'Injured'),
        ('Suspended', 'Suspended'),
        ('Inactive', 'Inactive'),
    ]

    athlete_id = models.BigAutoField(primary_key=True)
    # ON DELETE SET NULL requires null=True
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='athletes')
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    jersey_number = models.CharField(max_length=10, null=True, blank=True)
    position_or_specialty = models.CharField(max_length=50, null=True, blank=True)
    contract_start = models.DateField(null=True, blank=True)
    contract_end = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
#-------------------------------------------------------------------------
#Staff Table
class Staff(models.Model):
    ROLE_CHOICES = [
        ('Head Coach', 'Head Coach'),
        ('Assistant Coach', 'Assistant Coach'),
        ('Physiotherapist', 'Physiotherapist'),
        ('Fitness Coach', 'Fitness Coach'),
        ('Analyst', 'Analyst'),
        ('Manager', 'Manager'),
    ]

    staff_id = models.BigAutoField(primary_key=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='staff')
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    license_level = models.CharField(max_length=50, null=True, blank=True)

    # Many-to-Many connection to Teams through the custom bridge model
    teams = models.ManyToManyField(Team, through='TeamStaff', related_name='staff_members')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"

#-----------------------------------------------------------------------------------
#TamStaff
class TeamStaff(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    assignment_start = models.DateField()
    assignment_end = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, default='Active')

    class Meta:
        unique_together = ('team', 'staff')

#---------------------------------------------------------------------------------
#Competition Table
class Competition(models.Model):
    TYPE_CHOICES = [
        ('League', 'League'),
        ('Tournament', 'Tournament'),
        ('Knockout', 'Knockout'),
        ('Friendly', 'Friendly'),
    ]

    competition_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    organizer = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

#-----------------------------------------------------------------------------------
#Match Table
class Match(models.Model):
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Live', 'Live'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
        ('Postponed', 'Postponed'),
    ]

    match_id = models.BigAutoField(primary_key=True)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, related_name='matches')
    match_datetime = models.DateTimeField()
    venue_name = models.CharField(max_length=150, null=True, blank=True)
    match_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Scheduled')
    referee_name = models.CharField(max_length=150, null=True, blank=True)
    final_score_summary = models.CharField(max_length=50, null=True, blank=True)
    
    # Bridge connection to teams
    teams = models.ManyToManyField(Team, through='MatchParticipant', related_name='matches')

    def __str__(self):
        return f"Match {self.match_id} - {self.match_datetime}"

#---------------------------------------------------------------------------
#MatchParticipant
class MatchParticipant(models.Model):
    SIDE_CHOICES = [
        ('Home', 'Home'),
        ('Away', 'Away'),
        ('Neutral', 'Neutral'),
    ]
    RESULT_CHOICES = [
        ('Win', 'Win'),
        ('Loss', 'Loss'),
        ('Draw', 'Draw'),
        ('Pending', 'Pending'),
    ]

    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    side = models.CharField(max_length=10, choices=SIDE_CHOICES, null=True, blank=True)
    score_outcome = models.IntegerField(default=0)
    result_status = models.CharField(max_length=10, choices=RESULT_CHOICES, null=True, blank=True)

    class Meta:
        unique_together = ('match', 'team')
#----------------------------------------------------------------------------------
#PerformanceMetric Table
class PerformanceMetric(models.Model):
    metric_id = models.BigAutoField(primary_key=True)
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='performance_metrics')
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='performance_metrics')
    minutes_played = models.IntegerField(default=0)
    points_scored = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    fouls_committed = models.IntegerField(default=0)
    # Using Django's built-in native JSONField to handle the custom JSON data
    customized_stats_json = models.JSONField(null=True, blank=True)

#--------------------------------------------------------------------------------
#TournamentStanding
class TournamentStanding(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, related_name='standings')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='standings')
    matches_played = models.IntegerField(default=0)
    matches_won = models.IntegerField(default=0)
    matches_drawn = models.IntegerField(default=0)
    matches_lost = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    goals_or_points_for = models.IntegerField(default=0)
    goals_or_points_against = models.IntegerField(default=0)

    class Meta:
        unique_together = ('competition', 'team')

#----------------------------------------------------------------------------
#Injure Table
class Injury(models.Model):
    SEVERITY_CHOICES = [
        ('Mild', 'Mild'),
        ('Moderate', 'Moderate'),
        ('Severe', 'Severe'),
    ]

    injury_id = models.BigAutoField(primary_key=True)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='injuries')
    match = models.ForeignKey(Match, on_delete=models.SET_NULL, null=True, blank=True, related_name='injuries')
    injury_date = models.DateField()
    description = models.TextField(null=True, blank=True)
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES, null=True, blank=True)
    estimated_recovery_date = models.DateField(null=True, blank=True)
    actual_return_date = models.DateField(null=True, blank=True)