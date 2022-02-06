from django.db import models

# Create your models here.

class Lender(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length = 200, blank=False, null=False)
    code = models.CharField(max_length = 3, blank=False, null=False)
    upfront_commission_rate = models.FloatField(blank=False, null=False)
    trial_commission_rate = models.FloatField(blank=False, null=False)
    active = models.BooleanField(blank=False, null=False)

    class Meta:
        db_table = 'lender'
        verbose_name = 'lender'
        verbose_name_plural = 'lenders'
        ordering = ['id']

    def __str__(self):
        return self.name