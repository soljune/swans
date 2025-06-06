from django.db import models
from django.contrib.auth.models import User  # Make sure this import is present

class SwimWorkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    distance_meters = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()
    STROKE_CHOICES = [
        ('freestyle', 'Freestyle'),
        ('breaststroke', 'Breaststroke'),
        ('backstroke', 'Backstroke'),
        ('butterfly', 'Butterfly'),
        ('other', 'Other'),
    ]
    stroke_type = models.CharField(max_length=20, choices=STROKE_CHOICES)
    notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Workout by {self.user.username} on {self.date}"

class Pool(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    open_time = models.TimeField()
    close_time = models.TimeField()
    entry_price = models.DecimalField(max_digits=6, decimal_places=2)
    has_changing_room = models.BooleanField(default=False)
    has_restaurant = models.BooleanField(default=False)
    has_parking = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.address