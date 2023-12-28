from django.db import models

class Player(models.Model):
    """
    Player
    A class model for a player
    """
    Name = models.CharField(max_length=255,null=True)
    Nationality = models.CharField(max_length=50,null=True)
    National_Position = models.CharField(max_length=5,null=True)
    National_Kit = models.PositiveIntegerField(null=True)
    Club = models.CharField(max_length=255,null=True)
    Club_Position = models.CharField(max_length=5,null=True)
    Club_Kit = models.PositiveIntegerField(null=True)
    Club_Joining = models.CharField(null=True)
    Contract_Expiry = models.PositiveIntegerField(null=True)
    Rating = models.PositiveIntegerField(null=True)
    Height = models.CharField(max_length=10,null=True)
    Weight = models.CharField(max_length=10,null=True)
    Preffered_Foot = models.CharField(max_length=10,null=True)
    Birth_Date = models.CharField(null=True)
    Age = models.PositiveIntegerField(null=True)
    Preffered_Position = models.CharField(max_length=10,null=True)
    Work_Rate = models.CharField(max_length=20,null=True)
    Weak_foot = models.PositiveIntegerField(null=True)
    Skill_Moves = models.PositiveIntegerField(null=True)
    Ball_Control = models.PositiveIntegerField(null=True)
    Dribbling = models.PositiveIntegerField(null=True)
    Marking = models.PositiveIntegerField(null=True)
    Sliding_Tackle = models.PositiveIntegerField(null=True)
    Standing_Tackle = models.PositiveIntegerField(null=True)
    Aggression = models.PositiveIntegerField(null=True)
    Reactions = models.PositiveIntegerField(null=True)
    Attacking_Position = models.PositiveIntegerField(null=True)
    Interceptions = models.PositiveIntegerField(null=True)
    Vision = models.PositiveIntegerField(null=True)
    Composure = models.PositiveIntegerField(null=True)
    Crossing = models.PositiveIntegerField(null=True)
    Short_Pass = models.PositiveIntegerField(null=True)
    Long_Pass = models.PositiveIntegerField(null=True)
    Acceleration = models.PositiveIntegerField(null=True)
    Speed = models.PositiveIntegerField(null=True)
    Stamina = models.PositiveIntegerField(null=True)
    Strength = models.PositiveIntegerField(null=True)
    Balance = models.PositiveIntegerField(null=True)
    Agility = models.PositiveIntegerField(null=True)
    Jumping = models.PositiveIntegerField(null=True)
    Heading = models.PositiveIntegerField(null=True)
    Shot_Power = models.PositiveIntegerField(null=True)
    Finishing = models.PositiveIntegerField(null=True)
    Long_Shots = models.PositiveIntegerField(null=True)
    Curve = models.PositiveIntegerField(null=True)
    Freekick_Accuracy = models.PositiveIntegerField(null=True)
    Penalties = models.PositiveIntegerField(null=True)
    Volleys = models.PositiveIntegerField(null=True)
    GK_Positioning = models.PositiveIntegerField(null=True)
    GK_Diving = models.PositiveIntegerField(null=True)
    GK_Kicking = models.PositiveIntegerField(null=True)
    GK_Handling = models.PositiveIntegerField(null=True)
    GK_Reflexes = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = "Players"

    def __str__(self):
        return self.Name
