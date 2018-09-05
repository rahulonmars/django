from django.db import models

# Create your models here.

class Table1(models.Model):
    id = models.AutoField(primary_key=True)
    c_date = models.DateTimeField('Date Changed',auto_now=True)
    fname = models.CharField('First Name',max_length=200)
    email = models.CharField('Email ID',max_length =300)

    def __str__(self):
        return "First Name is : "+self.fname

class Table2(models.Model):
    id_2 = models.ForeignKey(Table1, on_delete=models.CASCADE)
    lname = models.CharField('Last Name',max_length=200)
    sex = models.CharField('Sex',max_length =5)

    def __str__(self):
        return "Last Name is : "+self.lname