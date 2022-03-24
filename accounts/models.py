from django.db import models

# Create your models here.

class customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class product(models.Model):
    CATEGORY = (
        ("Ondoor", "Indoor"),
        ("Out door", "Out door"),
    )

    name            = models.CharField(max_length=200, null=True)
    price           = models.FloatField(null=True)
    category        = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description     = models.CharField(max_length=200, null=True)
    date_created    = models.DateTimeField(auto_now_add=True, null=True)

class order(models.Model):
    STATUS = (
        ("Pending", "Pending"),
        ("Out for delivery", "Out for delivery"),
        ("Delivered", "Delivered"),
    )

    # customer =
    # product =
    date_created    = models.DateTimeField(auto_now_add=True, null=True)
    status          = models.CharField(max_length=200, null=True, choices=STATUS)