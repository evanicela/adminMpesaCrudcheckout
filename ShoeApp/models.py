from django.db import models

# Create your models here.
class Shoe(models.Model):
    shoename = models.CharField(db_column='shoename', max_length=100, blank=False)
    description = models.TextField(db_column='description', max_length=1000, blank=False)
    price = models.CharField(db_column='price', max_length=100, blank=False)
    imageurl = models.CharField(db_column='imageurl', max_length=1000, blank=False)

    class Meta:
        db_table = 'shoe'
        verbose_name = 'Shoe'
        verbose_name_plural = 'Shoes'

    def __unicode__(self):
        return self.shoename

    def __str__(self):
        return self.shoename


class Checkout(models.Model):
    transactionid = models.CharField(db_column='transactionid', max_length=100, blank=False)
    amount = models.CharField(db_column='amount', max_length=100, blank=False)
    phone = models.CharField(db_column='phone', max_length=100, blank=False)

    class Meta:
        db_table = 'checkout'
        verbose_name = 'checkout'
        verbose_name_plural = 'checkouts'

    def __unicode__(self):
        return self.transactionid

    def __str__(self):
        return self.transactionid