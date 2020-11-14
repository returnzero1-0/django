from django.db import models

# Create your models here.

class TableUser(models.Model):
    fname=models.TextField()
    lname=models.TextField()
    email=models.TextField()
    mobile=models.IntegerField()
    password=models.TextField()

   # objects = TableUserManager()

    #class Meta:
        #db_table = u'table_user'