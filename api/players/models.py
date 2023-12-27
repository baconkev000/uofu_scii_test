from django.db import models

class Player(models.Model):
    """
    Player
    A class model for a player
    """
    Name = models.CharField(max_length=255)
    Nationality = models.CharField(max_length=50)
    National_Position = models.CharField(max_length=5)
    National_Kit = models.PositiveIntegerField()
    Club = models.CharField(max_length=255)
    Club_Position = models.CharField(max_length=5)
    Club_Kit = models.PositiveIntegerField()
    Club_Joining = models.CharField()
    Contract_Expiry = models.PositiveIntegerField()
    Rating = models.PositiveIntegerField()
    Height = models.CharField(max_length=10)
    Weight = models.CharField(max_length=10)
    Preffered_Foot = models.CharField(max_length=10)
    Birth_Date = models.CharField()
    Age = models.PositiveIntegerField()
    Preffered_Position = models.CharField(max_length=10)
    Work_Rate = models.CharField(max_length=20)
    Weak_foot = models.PositiveIntegerField()
    Skill_Moves = models.PositiveIntegerField()
    Ball_Control = models.PositiveIntegerField()
    Dribbling = models.PositiveIntegerField()
    Marking = models.PositiveIntegerField()
    Sliding_Tackle = models.PositiveIntegerField()
    Standing_Tackle = models.PositiveIntegerField()
    Aggression = models.PositiveIntegerField()
    Reactions = models.PositiveIntegerField()
    Attacking_Position = models.PositiveIntegerField()
    Interceptions = models.PositiveIntegerField()
    Vision = models.PositiveIntegerField()
    Composure = models.PositiveIntegerField()
    Crossing = models.PositiveIntegerField()
    Short_Pass = models.PositiveIntegerField()
    Long_Pass = models.PositiveIntegerField()
    Acceleration = models.PositiveIntegerField()
    Speed = models.PositiveIntegerField()
    Stamina = models.PositiveIntegerField()
    Strength = models.PositiveIntegerField()
    Balance = models.PositiveIntegerField()
    Agility = models.PositiveIntegerField()
    Jumping = models.PositiveIntegerField()
    Heading = models.PositiveIntegerField()
    Shot_Power = models.PositiveIntegerField()
    Finishing = models.PositiveIntegerField()
    Long_Shots = models.PositiveIntegerField()
    Curve = models.PositiveIntegerField()
    Freekick_Accuracy = models.PositiveIntegerField()
    Penalties = models.PositiveIntegerField()
    Volleys = models.PositiveIntegerField()
    GK_Positioning = models.PositiveIntegerField()
    GK_Diving = models.PositiveIntegerField()
    GK_Kicking = models.PositiveIntegerField()
    GK_Handling = models.PositiveIntegerField()
    GK_Reflexes = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "Players"

    def __str__(self):
        return self.Name
