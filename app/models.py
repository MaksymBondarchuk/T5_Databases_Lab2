from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=10000)

    def __unicode__(self):
        return self.name


class Bill(models.Model):
    amount = models.FloatField()
    average_amount_for_month = models.FloatField()

    def __unicode__(self):
        return str(self.amount)


class Time(models.Model):
    datetime = models.DateTimeField()
    at_day_time = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.datetime)


class Transaction(models.Model):
    user = models.ForeignKey(User)
    bill = models.ForeignKey(Bill)
    time = models.ForeignKey(Time)

    def __unicode__(self):
        return self.user.name