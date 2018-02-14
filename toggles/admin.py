from django.contrib import admin

# Register your models here.
from .models import FeatureFlag

admin.site.register(FeatureFlag)
