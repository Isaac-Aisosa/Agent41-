from .models import *
from django import forms


class ServiceFeePaymentForm(forms.ModelForm):
    class Meta:
        model = ServiceFeePayment
        fields = [
            'amount', 'res_apartment', 'com_apartment',

        ]

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(ServiceFeePaymentForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(ServiceFeePaymentForm, self).save(commit=False)
        inst.user = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst


class AgentFeePaymentForm(forms.ModelForm):
    class Meta:
        model = AgentFeePayment
        fields = [
            'amount', 'res_apartment', 'com_apartment',

        ]

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(AgentFeePaymentForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(AgentFeePaymentForm, self).save(commit=False)
        inst.user = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst


class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = [
            'amount', 'purpose',
        ]

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(ExpensesForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(ExpensesForm, self).save(commit=False)
        inst.user = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'message',
        ]

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(FeedbackForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(FeedbackForm, self).save(commit=False)
        inst.user = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst


class FeedbackForm2(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'message',
        ]
