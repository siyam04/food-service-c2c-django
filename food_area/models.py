from django.db import models


class Area(models.Model):
    """Area for Ordering and Providing"""
    area_name = models.CharField(max_length=100, blank=False)
    zip_code = models.PositiveSmallIntegerField()

    def __str__(self):
        """Returns Name of the Object"""
        return self.area_name


