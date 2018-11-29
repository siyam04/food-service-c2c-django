from django.db import models
# food_area App importing
from food_area.models import Area
# food_area App importing
from food_providers.models import CooKInfo
from food_users_profile.models import Profile
# food_items App importing
from food_items.models import FoodItems
# food_delivery App importing
from food_delivery.models import DeliveryPoint


class Client(models.Model):
    """Information of Clients"""
    client_name = models.CharField(max_length=100)
    role = models.ForeignKey(Profile, blank=False, on_delete=models.CASCADE)
    client_image = models.ImageField(blank=False, upload_to='images')
    client_contact_no = models.PositiveIntegerField(blank=False)
    area = models.ForeignKey(Area, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        """Returns Name of the Object"""
        return self.client_name


class Order(models.Model):
    client_info = models.ForeignKey(Client, on_delete=models.CASCADE)
    food_name = models.ForeignKey(FoodItems, on_delete=models.CASCADE, blank=False)
    provider = models.ForeignKey(CooKInfo, on_delete=models.CASCADE, blank=False)
    quantity = models.PositiveSmallIntegerField(blank=False)
    delivery_point = models.ForeignKey(DeliveryPoint, on_delete=models.CASCADE, blank=False)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        """Returns Name of the Object"""
        return str(self.food_name)





