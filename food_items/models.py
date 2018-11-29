from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
# food_area App importing
from food_area.models import Area
# food_providers App importing
from food_providers.models import CooKInfo
# food_delivery App importing
from food_delivery.models import DeliveryPoint
# food_delivery App importing
# from food_users_profile.models import Profile


class FoodCategory(models.Model):
    """Food Category"""
    category_name = models.CharField(max_length=50)

    class Meta:
        """Admin Display Name"""
        verbose_name_plural = 'Food Categories'

    def __str__(self):
        """Returns Name of the Object"""
        return self.category_name


class FoodItems(models.Model):
    """All Food Items"""

    # Status of items
    ITEM_STATUS = (
        ('Available', 'AVAILABLE'),
        ('Sold', 'SOLD'),
    )

    # Database Attributes
    name = models.CharField(max_length=100, blank=False)
    food_image = models.ImageField(blank=False, upload_to='images')
    category = models.ForeignKey(FoodCategory, blank=False, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(blank=False)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    provider = models.ForeignKey(CooKInfo, on_delete=models.CASCADE)
    delivery_point = models.ForeignKey(DeliveryPoint, on_delete=models.CASCADE)
    minimum_quantity = models.PositiveSmallIntegerField(default=1, blank=False)
    posted_at = models.DateTimeField(auto_now=False, auto_now_add=True, blank=False)
    slug = models.SlugField(null=True)
    status = models.CharField(max_length=20, choices=ITEM_STATUS, default='AVAILABLE')
    draft = models.BooleanField(default=False)

    class Meta:
        """Meta class for customizing this class"""
        ordering = ['-id']
        verbose_name_plural = 'Food Items'

    def __str__(self):
        """Returns the Name of an object"""
        return self.name


# Signals Passing before saving to the DataBase
# Slugify the Name of the Food
# def pre_save_receiver(instance, **kwargs):
#     if not instance.slug and instance.name:
#         instance.slug = slugify(instance.name)


# Connecting with Signal
# pre_save.connect(pre_save_receiver, sender=FoodItems)


