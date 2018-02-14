from django.db import models


# Create your models here.
class FeatureFlag(models.Model):
    feature_key = models.CharField(max_length=200, unique=True)
    feature_value = models.CharField(max_length=200)

    def __str__(self):
        return self.feature_key + ' ' + self.feature_value
