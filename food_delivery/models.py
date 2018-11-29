from django.db import models
# food_area App importing
from food_area.models import Area


class DeliveryPoint(models.Model):
    """Information of who will deliver the Foods"""
    delivery_point_name = models.CharField(max_length=100, blank=False)
    delivery_point_image = models.ImageField(blank=False, upload_to='images')
    delivery_point_contact_no = models.PositiveIntegerField(blank=False)
    delivery_point_address = models.CharField(max_length=100, blank=False)
    area = models.ForeignKey(Area, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        """Returns Name of the Object"""
        return self.delivery_point_name
