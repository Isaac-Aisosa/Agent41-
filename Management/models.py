from django.conf import settings
from django.db import models
from Apartments.models import ResidentialApartment, CommercialApartment, ResidentialApartmentRequest, \
    CommercialApartmentRequest


class Agent41Details(models.Model):
    web_address = models.URLField(verbose_name='Web Address', null=True, blank=True, )
    phone = models.CharField(max_length=15, verbose_name='customer service phone', null=True, blank=True, )
    whatsapp = models.CharField(max_length=15, verbose_name='whatsapp number', null=True, blank=True, )
    email = models.EmailField(verbose_name='Email', null=True, blank=True, )
    agent_policy = models.TextField(verbose_name="agent policy", null=True, blank=True,
                                    default="agent policy should be wrinting here.")
    landlord_policy = models.TextField(verbose_name="landlord policy", null=True, blank=True,
                                       default="landlord policy should be wrinting here.")
    policy = models.TextField(verbose_name="policy", null=True, blank=True,
                              default="policy should be wrinting here.")
    about = models.TextField(verbose_name="About Agent41", null=True, blank=True,
                             default="about Agent41")
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    address = models.CharField(max_length=500, verbose_name='office Address', null=True, blank=True,
                               default="40 Golden palace sabo Auchi, edo state.")

    def __str__(self):
        return f'Agent41Details ({self.pk})'


class Agent41Pricing(models.Model):
    percentage = models.IntegerField(verbose_name='Apartment Percentage', null=True, blank=True, )
    commission = models.IntegerField(verbose_name='Agent Commission', null=True, blank=True, )
    service_fee = models.BigIntegerField(verbose_name='Service Fee', null=True, blank=True, )

    def __str__(self):
        return f'Agent41Pricing ({self.pk})'


class ServiceFeePayment(models.Model):
    amount = models.BigIntegerField(null=False, blank=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="staff_paid_to", on_delete=models.CASCADE, )
    res_apartment = models.ForeignKey(ResidentialApartmentRequest, related_name="paid_for_res",
                                      on_delete=models.CASCADE, null=True, blank=True, )
    com_apartment = models.ForeignKey(CommercialApartmentRequest, related_name="paid_for_comm",
                                      on_delete=models.CASCADE, null=True, blank=True, )
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'ServiceFeePayment ({self.res_apartment}{self.com_apartment})'


class AgentFeePayment(models.Model):
    amount = models.BigIntegerField(null=False, blank=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="paid_to_Agent", on_delete=models.CASCADE, )
    res_apartment = models.ForeignKey(ResidentialApartmentRequest, related_name="paid_agent_res",
                                      on_delete=models.CASCADE, null=True, blank=True, )
    com_apartment = models.ForeignKey(CommercialApartmentRequest, related_name="paid_agent_comm",
                                      on_delete=models.CASCADE, null=True, blank=True, )
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'AgentFeePayment ({self.res_apartment}{self.com_apartment})'


class AgentPaymentUnit(models.Model):
    unit = models.IntegerField(default=100)
    payment_threshold = models.BigIntegerField(default=1000)

    def __str__(self):
        return f'AgentPaymentUnit: {self.unit}'


class Expenses(models.Model):
    amount = models.BigIntegerField(default=0, blank=False, null=False)
    purpose = models.TextField(max_length=1000, blank=False, null=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="Ex_Reg_by", on_delete=models.CASCADE, )
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'Expenses: {self.amount}'


class Feedback(models.Model):
    message = models.TextField(max_length=255, blank=False, null=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="feedback_sender", on_delete=models.CASCADE, blank=True, null=True)
    unknown = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'Feedback: {self.user}'
