from django.db import models

# Create your models here.
# models.py

from django.db import models

class WheelSpecification(models.Model):
    form_number = models.CharField(max_length=100, unique=True)
    submitted_by = models.CharField(max_length=100)
    submitted_date = models.DateField()

    tread_diameter_new = models.CharField(max_length=50)
    last_shop_issue_size = models.CharField(max_length=50)
    condemning_dia = models.CharField(max_length=50)
    wheel_gauge = models.CharField(max_length=50)
    variation_same_axle = models.CharField(max_length=50)
    variation_same_bogie = models.CharField(max_length=50)
    variation_same_coach = models.CharField(max_length=50)
    wheel_profile = models.CharField(max_length=100)
    intermediate_wwp = models.CharField(max_length=50)
    bearing_seat_diameter = models.CharField(max_length=100)
    roller_bearing_outer_dia = models.CharField(max_length=50)
    roller_bearing_bore_dia = models.CharField(max_length=50)
    roller_bearing_width = models.CharField(max_length=50)
    axle_box_housing_bore_dia = models.CharField(max_length=50)
    wheel_disc_width = models.CharField(max_length=50)

    status = models.CharField(max_length=20, default='Saved')

    def __str__(self):
        return self.form_number
