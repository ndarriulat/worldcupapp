from django.db import models
from django.utils import timezone

# Team. Contains name, group number, points and players
class Team(models.Model):
    name = models.CharField(max_length=200)
    group_number = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    victories = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)

# Result. Contains two teams and their score
class Result(models.Model):
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='%(class)s_requests_created')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE)
    team1_score = models.IntegerField(default=0)
    team2_score = models.IntegerField(default=0)
    date = models.DateTimeField('Match date and time')

# Player. Contains name and team
class Player(models.Model):
    name = models.CharField(max_length=200)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

# User. Contains username, password
class User(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

# Prognostic. Contains two teams,
# prognostic for team 1, prognostic for team 2 and the user
class Prognostic(models.Model):
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='%(class)s_requests_created')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE)
    team1_prognostic = models.IntegerField(default=0)
    team2_prognostic = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)