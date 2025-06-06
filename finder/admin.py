from django.contrib import admin

# import models
from .models import SwimWorkout,Pool
# Register your models here.
admin.site.register(SwimWorkout)
admin.site.register(Pool)