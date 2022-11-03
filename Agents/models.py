from django.conf import settings
from django.db import models


# Create your models here.


class PaymentDetail(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='account', on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, verbose_name='Account number', default='account number',
                                      null=False, blank=False)
    account_name = models.CharField(max_length=100, verbose_name='Account name', default='account name', null=False,
                                    blank=False)
    bank = models.CharField(max_length=30, verbose_name='Bank', default='bank', null=False, blank=False)
    paid = models.BigIntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f'{self.user} '


class RequestPayment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='raccount', on_delete=models.CASCADE)
    Amount = models.BigIntegerField(default=0)
    paid = models.BooleanField(default=False)
    pending = models.BooleanField(default=False)
    failed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.user} '
