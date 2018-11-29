from django.db import models
# food_area App importing
from food_area.models import Area


class CooKInfo(models.Model):
    """Information od Cook who Provide the Foods"""
    cook_name = models.CharField(max_length=100, blank=False)
    cook_image = models.ImageField(blank=False, upload_to='images')
    contact_no = models.PositiveIntegerField(blank=False)
    area = models.ForeignKey(Area, blank=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Cook Infos'

    def __str__(self):
        """Returns Name of the Object"""
        return self.cook_name
