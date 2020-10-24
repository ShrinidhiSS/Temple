from django.db import models

class Church(models.Model):
    gender_type = (
        ('Male', 'Male'),
        ('Female','Female'),
    )
    relation_type = (
        ('Wife','Wife'),
        ('Son','Son'),
        ('Daughter','Daughter'),
        ('Husband','Husband'),
    )
    status_type = (
        ('Alive','Alive'),
        ('Not Alive','NOt Alive'),
    )
    house_type = (
        ('Own','Own'),
        ('Rent','Rent'),
    )

    unique_id = models.CharField(max_length=100)
    anbiyam = models.IntegerField(null=True,blank=True)
    name = models.CharField(max_length=100,null=True)
    # parent_tag =
    gender = models.CharField(max_length=100,null=True,choices=gender_type,blank=True)
    relationship = models.CharField(max_length=100,null=True,choices=relation_type,blank=True)
    aadhaar_no = models.CharField(max_length=100,null=True,blank=True)
    status = models.CharField(max_length=100,null=True,choices=status_type,blank=True)
    place = models.CharField(max_length=100,null=True,blank=True)
    district = models.CharField(max_length=100,null=True,default='Kanyakumari')
    state = models.CharField(max_length=100,null=True,default='Tamil Nadu')
    country = models.CharField(max_length=100,null=True,default='India')
    pincode = models.IntegerField(null=True,default=629701,blank=True)
    house_status = models.CharField(max_length=100,null=True,choices=house_type,blank=True)


    def __str__(self):
        return self.name
