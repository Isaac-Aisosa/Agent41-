from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from Agents.form import agent_SignUpForm, AgentProfilesForm, AgentResidentialApartmentForm, \
    AgentCommercialApartmentForm, PaymentEditForm, PaymentForm, AgentEditForm
from Agents.models import PaymentDetail, RequestPayment
from Apartments.models import ResidentialApartment, CommercialApartment
from Management.models import AgentPaymentUnit
from User_Profiles.models import UserProfiles


def agent_index(request):
    if request.user.is_authenticated:
        user = request.user
        profile = UserProfiles.objects.get(user=user)
        res_apartment = ResidentialApartment.objects.all().filter(user=user).order_by("-timestamp")
        comm_apartment = CommercialApartment.objects.all().filter(user=user).order_by("-timestamp")
        context = {
            "profile": profile,
            "res_apartment": res_apartment,
            "comm_apartment": comm_apartment,
        }
        return render(request, "agent_index.html", context)
    else:
        return redirect('agent_login')


def agent_profile(request):
    if request.user.is_authenticated:
        user = request.user
        profile = UserProfiles.objects.get(user=user)
        pay = AgentPaymentUnit.objects.get(id=1)
        pay_unit = pay.unit
        reg_apartment = profile.apartment
        pay_threshold = pay.payment_threshold
        payment = PaymentDetail.objects.get(user=user)
        paid = payment.paid
        w = reg_apartment * pay_unit
        rw = w - paid
        wallet = rw
        p_request = RequestPayment.objects.all().filter(user=request.user)

        context = {
            "profile": profile,
            "pay_threshold": pay_threshold,
            "wallet": wallet,
            "paid": paid,
            "pay_unit": pay_unit,
            "reg_apartment": reg_apartment,
            "bank": payment,
            "p_request": p_request,

        }
        return render(request, "agent_profile.html", context)
    else:
        return redirect('agent_login')


@login_required
def edit_agent_profile(request):
    user = get_object_or_404(UserProfiles, user=request.user)
    edit_profile = AgentEditForm(instance=user)
    if request.method == "POST":
        edit_profile = AgentEditForm(request.POST, request.FILES, instance=user)
        if edit_profile.is_valid():
            edit_profile.save()
            return redirect('agent_profile2')

    context = {'form': edit_profile}

    return render(request, 'edit_agent_profile.html', context)


def requestpay(request):
    user = request.user
    profile = UserProfiles.objects.get(user=user)
    pay = AgentPaymentUnit.objects.get(id=1)
    pay_unit = pay.unit
    reg_apartment = profile.apartment
    payment = PaymentDetail.objects.get(user=user)
    paid = payment.paid
    w = reg_apartment * pay_unit
    rw = w - paid
    wallet = rw
    request = RequestPayment.objects.all().filter(user=request.user)
    if request:
        rrequest = RequestPayment.objects.get(user=user)
        rrequest.Amount = wallet
        rrequest.pending = True
        rrequest.paid = False
        rrequest.failed = False
        rrequest.save()
        return redirect('agent_profile2')
    else:
        newrequest = RequestPayment()
        newrequest.Amount = wallet
        newrequest.user = user
        newrequest.paid = False
        newrequest.failed = False
        newrequest.pending = True
        newrequest.save()
        return redirect('agent_profile2')


@login_required
def edit_payment(request):
    user = get_object_or_404(PaymentDetail, user=request.user)
    payment_edit_form = PaymentEditForm(instance=user)
    if request.method == "POST":
        payment_edit_form = PaymentEditForm(request.POST, request.FILES, instance=user)
        if payment_edit_form.is_valid():
            payment_edit_form.save()
            return redirect('agent_profile2')

    context = {'payment_edit_form': payment_edit_form}

    return render(request, 'edit_payment.html', context)


def paymentform(request):
    form = PaymentForm(request.POST)
    form.instance.user = request.user
    if form.is_valid():
        form.save()
        return redirect('agent_index')
    else:
        form = PaymentForm()
    return render(request, 'paymentform.html', {'form': form})


def agent_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('agent_index')

    return render(request, 'agent_login.html ')


def agent_signup(request):
    if request.method == 'POST':
        form = agent_SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('agent_profile')
    else:
        form = agent_SignUpForm()

    context = {

        'form': form,

    }
    return render(request, 'agent_signup.html', context)


@login_required
def create_agent_profile(request):
    form = AgentProfilesForm(request.POST, request.FILES, user=request.user)
    if form.is_valid():
        instance = form.save()
        profile = UserProfiles.objects.get(pk=instance.pk)
        profile.landlord = False
        profile.agent = True
        profile.staff = False
        profile.admin = False
        profile.save()
        return redirect('paymentform')
    else:
        form = AgentProfilesForm(user=request.user)

    return render(request, 'agentProfiles.html', {"form": form, })


@login_required
def agent_select_form(request):
    context = {

    }
    return render(request, 'agent_select_form.html', context)


@login_required
def agent_residential_apartment_form(request):
    form = AgentResidentialApartmentForm(request.POST, request.FILES, user=request.user)
    if form.is_valid():
        form.save()
        return redirect('agent_index')
    else:
        form = AgentResidentialApartmentForm(user=request.user)
    return render(request, 'agent_residential_apartment_form.html', {"form": form, })


@login_required
def agent_commercial_apartment_form(request):
    form = AgentCommercialApartmentForm(request.POST, request.FILES, user=request.user)
    if form.is_valid():
        form.save()
        return redirect('agent_index')
    else:
        form = AgentCommercialApartmentForm(user=request.user)
    return render(request, 'agent_commercial_apartment_form.html', {"form": form, })
