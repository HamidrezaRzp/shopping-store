from django.db import models

class User(models.Model):
    firstname = models.CharField( max_length=100 )
    lastname  = models.CharField( max_length=100 )
    joined_date = models.DateField( null=True )
    national_code = models.IntegerField( null=True )

    def __str__(self):
        return f"{self.firstname} {self.lastname}"