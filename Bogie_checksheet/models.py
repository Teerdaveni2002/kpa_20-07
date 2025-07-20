from django.db import models

# Create your models here.
class BogieDetails(models.Model):
    bogie_no = models.CharField(max_length=100)
    maker_year_built = models.CharField(max_length=100)
    incoming_div_and_date = models.CharField(max_length=100)
    deficit_components = models.TextField(blank=True)
    date_of_ioh = models.DateField()


class BogieChecksheet(models.Model):
    CONDITION_CHOICES = [
        ("Good", "Good"),
        ("Cracked", "Cracked"),
        ("Worn Out", "Worn Out"),
        ("Damaged", "Damaged"),
        ("Other", "Other"),
    ]
    BOLSTER_CHOICES = [
        ('Good', 'Good'),
        ('Cracked', 'Cracked'),
        ('Worn Out', 'Worn Out'),
        ('Bent', 'Bent'),
        ('Other', 'Other'),
    ]
    BOLSTER_SUSPENSION = [
        ('Good', 'Good'),
        ('Cracked', 'Cracked'),
        ('Corroded', 'Corroded'),
        ('Other', 'Other'),
    ]
    AXILE_GUIDE_CHOICES = [
        ('Good', 'Good'),
        ('Worn', 'Worn'),
        ('Misalign', 'Misalign'),
        ('Other', 'Other'),
    ]


    axile_guide_assembly = models.CharField(max_length=50, choices=AXILE_GUIDE_CHOICES)
    bogie_details = models.OneToOneField(BogieDetails, on_delete=models.CASCADE)
    axle_guide = models.CharField(max_length=50, choices=AXILE_GUIDE_CHOICES)
    bogieFrameCondition = models.CharField(max_length=100, choices=CONDITION_CHOICES)
    bolster = models.CharField(max_length=50, choices=BOLSTER_CHOICES)
    bolster_suspension_bracket = models.CharField(max_length=50, choices=BOLSTER_SUSPENSION)
    lower_spring_seat = models.CharField(max_length=50, choices = CONDITION_CHOICES)
    protective_tubes =  models.CharField(max_length=50, choices=CONDITION_CHOICES)
    anchor_links = models.CharField(max_length=50, choices=CONDITION_CHOICES)
    side_bearer = models.CharField(max_length=50, choices=CONDITION_CHOICES)
class BMBCChecksheet(models.Model):
    CONDITION_CHOICES = [
        ("Good", "Good"),
        ("Cracked", "Cracked"),
        ("Worn Out", "Worn Out"),
        ("Damaged", "Damaged"),
        ("Other", "Other"),
    ]
    adjusting_tube = models.CharField(max_length=50, choices=CONDITION_CHOICES)
    cylinder_body = models.CharField(max_length=50, choices=CONDITION_CHOICES)
    piston_trunnion = models.CharField(max_length=50, choices=CONDITION_CHOICES)
    plunger_spring = models.CharField(max_length=50, choices=CONDITION_CHOICES)
    tee_bolt = models.CharField(max_length=50, choices=CONDITION_CHOICES)
    pawl = models.CharField(max_length=50, choices=CONDITION_CHOICES)
    pawl_spring = models.CharField(max_length=50, choices=CONDITION_CHOICES)
    dust_excluder = models.CharField(max_length=50, choices=CONDITION_CHOICES)

class BogieFormSubmission(models.Model):

    form_number = models.CharField(max_length=100, unique=True)
    inspection_by = models.CharField(max_length=100)
    inspection_date = models.DateField()
    bogie_checksheet = models.OneToOneField(BogieChecksheet, on_delete=models.CASCADE)
    bmbc_checksheet = models.OneToOneField(BMBCChecksheet, on_delete=models.CASCADE)



