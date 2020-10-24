from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Church(models.Model):
    status_type = (
        ('Widow','Widow'),
        ('Unsupported','Unsupported'),
    )
    marriage_type = (
        ('Single','Single'),
        ('Married','Married'),
    )
    house_type = (
        ('odu','odu'),
        ('koorai','koorai'),
        ('concrete','concrete'),
        ('rent','rent'),
    )
    property_type = (
        ('land','land'),
        ('farmland','farmland'),
        ('vehiicle','vehicle'),
        ('domestic_animals','domestic_animals'),
    )
    job_type = (
        ('govt','govt'),
        ('private','private'),
        ('farming','farming'),
        ('construction','construction'),
    )
    job_loc_type = (
        ('local','local'),
        ('abroad','abroad'),
        ('veliyoor','veliyoor'),
    )
    things_type = (
        ('electricity','electricity'),
        ('computer','computer'),
        ('water','water'),
        ('toilet','toilet'),
    )
    family_head = models.CharField(max_length=100,null=True, blank=True)
    family_card_no = models.CharField(max_length=100,null=True, blank=True)
    phone_no = models.CharField(max_length=15,null=True, blank=True)
    name = models.CharField(max_length=50,null=True, blank=True)
    relationship = models.CharField(max_length=50,null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    dob = models.DateField(max_length=8,null=True, blank=True)
    education = models.CharField(max_length=100,null=True, blank=True)
    status = models.CharField(max_length=50, choices = status_type, null=True, blank=True)
    thirumuluku = models.CharField(max_length=100,null=True, blank=True)
    pudhunanmai = models.CharField(max_length=100,null=True, blank=True)
    urudhipoosudhal = models.CharField(max_length=100,null=True, blank=True)
    marriage = models.CharField(max_length=100, choices = marriage_type,null=True, blank=True)
    kuruthuvam = models.CharField(max_length=100,null=True, blank=True)
    note = models.CharField(max_length=200,null=True, blank=True)
    organization_member = models.CharField(max_length=200,null=True, blank=True)
    nalavariya_urupinar = models.CharField(max_length=100,null=True, blank=True)
    organ_donation = models.CharField(max_length=100,null=True, blank=True)
    vangi_kanaku = models.CharField(max_length=100,null=True, blank=True)
    vilayatu = models.CharField(max_length=100,null=True, blank=True)
    udal_oonam = models.CharField(max_length=100,null=True, blank=True)
    thiran = models.CharField(max_length=100,null=True, blank=True)
    goal = models.CharField(max_length=100,null=True, blank=True)
    thiruviliyam = models.BooleanField(null=True, blank=True)
    kudumba_jebam = models.BooleanField(null=True, blank=True)
    maraikalvi = models.BooleanField(null=True, blank=True)
    bakthasabai_iyakkam = models.BooleanField(null=True, blank=True)
    arasiyal_eedubaadu = models.BooleanField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('church-detail',kwargs={'pk':self.pk})
