from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from Apartments.models import ResidentialApartment, CommercialApartment, ResidentialApartmentRequest, \
    CommercialApartmentRequest
from Agents.models import *
from Management.forms import ServiceFeePaymentForm, AgentFeePaymentForm, ExpensesForm, FeedbackForm, FeedbackForm2
from Management.models import Agent41Details, Agent41Pricing, ServiceFeePayment, AgentFeePayment, AgentPaymentUnit, \
    Expenses, Feedback
from User_Profiles.models import UserProfiles
import datetime
from django.utils.timezone import now


# Create your views here.

def dashboard(request):
    if request.user.is_authenticated:
        res_apartment = ResidentialApartment.objects.all().filter(approved=True)
        com_apartment = CommercialApartment.objects.all().filter(approved=True)
        pending_res = ResidentialApartment.objects.all().filter(approved=False, unapproved=False).count()
        pending_com = CommercialApartment.objects.all().filter(approved=False, unapproved=False).count()
        pending_apartment = pending_com + pending_res
        landlord = UserProfiles.objects.filter(landlord=True).count()
        agent = UserProfiles.objects.filter(agent=True).count()
        apartment_request_res = ResidentialApartmentRequest.objects.filter(comfirmed=False).count()
        apartment_request_comm = CommercialApartmentRequest.objects.filter(comfirmed=False).count()
        apartment_request = apartment_request_comm + apartment_request_res
        agent_payment_request = RequestPayment.objects.filter(pending=True)
        feedback = Feedback.objects.filter(timestamp__gte=datetime.date.today())
        context = {

            "res_apartment": res_apartment,
            "com_apartment": com_apartment,
            "pending_apartment": pending_apartment,
            "landlord": landlord,
            "apartment_request": apartment_request,
            "agent": agent,
            "agent_payment_request": agent_payment_request,
            "feedback": feedback,

        }
        return render(request, 'dashboard.html', context)
    else:
        return redirect('staff_login')


def staff_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('dashboard')

    return render(request, 'staff_login.html ')


@staff_member_required
@login_required
def management_res_apartment_request(request):
    apartment_request = ResidentialApartmentRequest.objects.filter(comfirmed=False).order_by("-timestamp")
    apartment_request_comm = CommercialApartmentRequest.objects.filter(comfirmed=False).order_by("-timestamp")

    context = {

        "apartment_request": apartment_request,
        "apartment_request_comm": apartment_request_comm,

    }
    return render(request, 'management_apartment_request.html', context)


@staff_member_required
@login_required
def management_all_apartment_request(request):
    apartment_request = ResidentialApartmentRequest.objects.all().order_by("-timestamp")
    apartment_request_comm = CommercialApartmentRequest.objects.all().order_by("-timestamp")

    context = {

        "apartment_request": apartment_request,
        "apartment_request_comm": apartment_request_comm,

    }
    return render(request, 'management_all_apartment_request.html', context)


@staff_member_required
@login_required
def management_daily_apartment_request(request):
    apartment_request = ResidentialApartmentRequest.objects.filter(timestamp__gte=datetime.date.today()).order_by(
        "-timestamp")
    apartment_request_comm = CommercialApartmentRequest.objects.filter(timestamp__gte=datetime.date.today()).order_by(
        "-timestamp")

    context = {

        "apartment_request": apartment_request,
        "apartment_request_comm": apartment_request_comm,

    }
    return render(request, 'management_daily_apartment_request.html', context)


@staff_member_required
@login_required
def management_weekly_apartment_request(request):
    date = datetime.datetime.today()
    week = date.strftime("%V")
    apartment_request = ResidentialApartmentRequest.objects.filter(timestamp__week=week).order_by(
        "-timestamp")
    apartment_request_comm = CommercialApartmentRequest.objects.filter(timestamp__week=week).order_by(
        "-timestamp")

    context = {

        "apartment_request": apartment_request,
        "apartment_request_comm": apartment_request_comm,

    }
    return render(request, 'management_weekly_apartment_request.html', context)


@staff_member_required
@login_required
def management_res_apartment_request_detail(request, id, pk):
    apartment_request = ResidentialApartmentRequest.objects.get(pk=id)
    apartment = ResidentialApartment.objects.get(pk=pk)
    registered = UserProfiles.objects.get(user=apartment.user)
    agent41_details = Agent41Details.objects.get(pk=1)
    agent41_pricing = Agent41Pricing.objects.get(pk=1)
    percent = agent41_pricing.percentage / 100 * apartment.price
    # request = get_object_or_404(ResidentialApartmentRequest, pk=id)
    # request.seen = True
    # request.save()
    context = {

        "apartment_request": apartment_request,
        "apartment": apartment,
        "registered": registered,
        "agent41_details": agent41_details,
        "agent41_pricing": agent41_pricing,
        "percent": percent,
    }
    return render(request, 'management_res_apartment_request_detail.html', context)


@staff_member_required
@login_required
def management_comm_apartment_request_detail(request, id, pk):
    apartment_request = CommercialApartmentRequest.objects.get(pk=id)
    apartment = CommercialApartment.objects.get(pk=pk)
    registered = UserProfiles.objects.get(user=apartment.user)
    agent41_details = Agent41Details.objects.get(pk=1)
    agent41_pricing = Agent41Pricing.objects.get(pk=1)
    percent = agent41_pricing.percentage / 100 * apartment.price
    # request = get_object_or_404(ResidentialApartmentRequest, pk=id)
    # request.seen = True
    # request.save()
    context = {

        "apartment_request": apartment_request,
        "apartment": apartment,
        "Registered": registered,
        "agent41_details": agent41_details,
        "agent41_pricing": agent41_pricing,
        "percent": percent,

    }
    return render(request, 'management_comm_apartment_request_detail.html', context)


@staff_member_required
@login_required
def management_apartment_pending(request):
    res_apartment = ResidentialApartment.objects.all().filter(approved=False, unapproved=False).order_by(
        "-timestamp")
    comm_apartment = CommercialApartment.objects.all().filter(approved=False, unapproved=False).order_by(
        "-timestamp")

    context = {

        "res_apartment": res_apartment,
        "comm_apartment": comm_apartment,

    }
    return render(request, 'management_apartment_pending.html', context)


@staff_member_required
@login_required
def management_res_apartment_detail(request, pk):
    apartment = ResidentialApartment.objects.get(pk=pk)
    registered = UserProfiles.objects.get(user=apartment.user)
    pricing = Agent41Pricing.objects.get(id=1)
    percent = pricing.percentage / 100 * apartment.price

    context = {
        "apartment": apartment,
        "registered": registered,
        "pricing": pricing,
        "percent": percent,

    }
    return render(request, 'management_res_apartment_detail.html', context)


@staff_member_required
@login_required
def management_comm_apartment_detail(request, pk):
    apartment = CommercialApartment.objects.get(pk=pk)
    registered = UserProfiles.objects.get(user=apartment.user)
    pricing = Agent41Pricing.objects.get(id=1)
    percent = pricing.percentage / 100 * apartment.price
    context = {
        "apartment": apartment,
        "registered": registered,
        "pricing": pricing,
        "percent": percent,

    }
    return render(request, 'management_comm_apartment_detail.html', context)


@staff_member_required
@login_required
def management_apartment_all(request):
    res_apartment = ResidentialApartment.objects.all().filter(approved=True, unapproved=False).order_by(
        "-timestamp")
    comm_apartment = CommercialApartment.objects.all().filter(approved=True, unapproved=False).order_by(
        "-timestamp")

    context = {

        "res_apartment": res_apartment,
        "comm_apartment": comm_apartment,

    }
    return render(request, 'management_apartment_all.html', context)


@staff_member_required
@login_required
def management_apartment_unapproved(request):
    res_apartment = ResidentialApartment.objects.all().filter(approved=False, unapproved=True).order_by(
        "-timestamp")
    comm_apartment = CommercialApartment.objects.all().filter(approved=False, unapproved=True).order_by(
        "-timestamp")
    context = {

        "res_apartment": res_apartment,
        "comm_apartment": comm_apartment,

    }
    return render(request, 'management_apartment_unapproved.html', context)


@staff_member_required
@login_required
def apartment_no_vacancy(request):
    res_apartment = ResidentialApartment.objects.all().filter(vacancy=0).order_by(
        "-timestamp")
    comm_apartment = CommercialApartment.objects.all().filter(vacancy=0).order_by(
        "-timestamp")
    context = {

        "res_apartment": res_apartment,
        "comm_apartment": comm_apartment,

    }
    return render(request, 'apartment_no_vacancy.html', context)


def search_apartment(request):
    details = Agent41Details.objects.get(pk=1)
    query = request.GET.get('search')
    if query is not None:
        lookups = Q(name__icontains=query) | Q(price__icontains=query) | Q(power__icontains=query) | \
                  Q(location__location__icontains=query) | Q(type__type__icontains=query) | \
                  Q(city__city__icontains=query) | Q(state__state__icontains=query) | Q(power__icontains=query) \
                  | Q(landlord_name__icontains=query) | Q(landlord_phone__iexact=query) | Q(Address__icontains=query)

        res_apartment = ResidentialApartment.objects.filter(lookups).distinct()
        comm_apartment = CommercialApartment.objects.filter(lookups).distinct()

        context = {
            "res_apartment": res_apartment,
            "comm_apartment": comm_apartment,
            'details': details,
            "query": query,

        }
        return render(request, 'search_apartments.html', context)


@staff_member_required
@login_required
def agent_list(request):
    agent = UserProfiles.objects.filter(agent=True).order_by("full_name")
    context = {
        "agent": agent,

    }
    return render(request, 'agent_list.html', context)


@staff_member_required
@login_required
def agent_details(request, pk):
    agent = UserProfiles.objects.get(pk=pk)
    user = agent.user
    profile = UserProfiles.objects.get(user=user)
    pay = AgentPaymentUnit.objects.get(id=1)
    pay_unit = pay.unit
    reg_apartment = profile.apartment
    payment = PaymentDetail.objects.get(user=user)
    paid = payment.paid
    w = reg_apartment * pay_unit
    rw = w - paid
    wallet = rw
    res_apartment = ResidentialApartment.objects.filter(user=agent.user)
    comm_apartment = CommercialApartment.objects.filter(user=agent.user)
    context = {
        "agent": agent,
        "res_apartment": res_apartment,
        "comm_apartment": comm_apartment,
        "paid": paid,
        "wallet": wallet,
    }
    return render(request, 'agent_details.html', context)


@staff_member_required
@login_required
def landlord_details(request, pk):
    landlord = UserProfiles.objects.get(pk=pk)
    res_apartment = ResidentialApartment.objects.filter(user=landlord.user)
    comm_apartment = CommercialApartment.objects.filter(user=landlord.user)
    context = {
        "landlord": landlord,
        "res_apartment": res_apartment,
        "comm_apartment": comm_apartment,

    }
    return render(request, 'landlord_details.html', context)


@staff_member_required
@login_required
def landlord_list(request):
    landlord = UserProfiles.objects.filter(landlord=True).order_by("full_name")
    context = {
        "landlord": landlord,

    }
    return render(request, 'landlord_list.html', context)


@staff_member_required
@login_required
def service_fee(request):
    form = ServiceFeePaymentForm(request.POST, request.FILES, user=request.user)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    else:
        form = ServiceFeePaymentForm(user=request.user)

    return render(request, 'service_fee.html', {"form": form, })


@staff_member_required
@login_required
def agent_fee(request):
    form = AgentFeePaymentForm(request.POST, request.FILES, user=request.user)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    else:
        form = AgentFeePaymentForm(user=request.user)

    return render(request, 'agent_fee.html', {"form": form, })


@staff_member_required
@login_required
def payment(request):
    return render(request, 'payments.html')


@staff_member_required
@login_required
def revenue_manager(request):
    d_service_fee = ServiceFeePayment.objects.filter(timestamp__gte=datetime.date.today()).order_by(
        "-timestamp")
    d_agent_fee = AgentFeePayment.objects.filter(timestamp__gte=datetime.date.today()).order_by(
        "-timestamp")
    d_service = d_service_fee.aggregate(d_service=Sum('amount'))['d_service']
    d_agent = d_agent_fee.aggregate(d_agent=Sum('amount'))['d_agent']

    t_service_fee = ServiceFeePayment.objects.all()
    t_agent_fee = AgentFeePayment.objects.all()
    t_service = t_service_fee.aggregate(t_service=Sum('amount'))['t_service']
    t_agent = t_agent_fee.aggregate(t_agent=Sum('amount'))['t_agent']

    d_expenses = Expenses.objects.filter(timestamp__gte=datetime.date.today()).order_by(
        "-timestamp")
    d_total = d_expenses.aggregate(total=Sum('amount'))['total']

    expenses = Expenses.objects.all()
    total = expenses.aggregate(total=Sum('amount'))['total']

    revenue = t_agent + t_service
    a_revenue = t_agent + t_service - total
    res_apartment = ResidentialApartment.objects.all().filter(approved=True)
    com_apartment = CommercialApartment.objects.all().filter(approved=True)

    t_res = res_apartment.aggregate(t_res=Sum('price'))['t_res']
    t_com = com_apartment.aggregate(t_com=Sum('price'))['t_com']
    apartment = t_res + t_com

    r_vacancy = res_apartment.aggregate(r_vacancy=Sum('vacancy'))['r_vacancy']
    c_vacancy = com_apartment.aggregate(c_vacancy=Sum('vacancy'))['c_vacancy']
    vacancy = r_vacancy + c_vacancy

    pricing = Agent41Pricing.objects.get(id=1)

    percent = pricing.percentage / 100 * apartment

    service = pricing.service_fee * vacancy

    est_revenue = service + percent

    context = {
        "d_service": d_service,
        "d_agent": d_agent,
        "revenue": revenue,
        "a_revenue": a_revenue,
        "percent": percent,
        "pricing": pricing,
        "service": service,
        "est_revenue": est_revenue,
        "d_total": d_total,
    }
    return render(request, 'revenue_manager.html', context)


@staff_member_required
@login_required
def agent_payment_request(request):
    rpay = RequestPayment.objects.filter(pending=True).order_by('-timestamp')
    context = {

        'rpay': rpay,

    }
    return render(request, 'agent_payment_request.html', context)


@staff_member_required
@login_required
def failed_payment(request):
    fpay = RequestPayment.objects.all().filter(failed=True).order_by('-timestamp')
    context = {

        'fpay': fpay,

    }
    return render(request, 'failed_payment.html', context)


@staff_member_required
@login_required
def paid_agent(request):
    fpay = RequestPayment.objects.filter(paid=True).order_by('-timestamp')
    tpay = PaymentDetail.objects.all()
    total_paid = tpay.aggregate(total_paid=Sum('paid'))['total_paid']
    context = {

        'fpay': fpay,
        'total_paid': total_paid,

    }
    return render(request, 'paid_user.html', context)


@staff_member_required
@login_required
def request_detail(request, pk):
    rpay = RequestPayment.objects.get(pk=pk)
    user = rpay.user
    acct = PaymentDetail.objects.get(user=user)
    profile = UserProfiles.objects.get(user=user)

    context = {
        'rpay': rpay,
        'acct': acct,
        'profile': profile,

    }
    return render(request, 'agent_request_detail.html', context)


@staff_member_required
@login_required
def paid(request, pk):
    rpay = RequestPayment.objects.get(pk=pk)
    rpay.pending = False
    rpay.paid = True
    rpay.failed = False
    rpay.save()
    user = rpay.user
    amount = rpay.Amount
    acct = PaymentDetail.objects.get(user=user)
    acct.paid += amount
    acct.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@staff_member_required
@login_required
def failed(request, pk):
    fpay = RequestPayment.objects.get(pk=pk)
    fpay.pending = False
    fpay.paid = False
    fpay.failed = True
    fpay.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@staff_member_required
@login_required
def expenses_list(request):
    expenses = Expenses.objects.filter(timestamp__gte=datetime.date.today()).order_by(
        "-timestamp")
    total = expenses.aggregate(total=Sum('amount'))['total']

    context = {
        "expenses": expenses,
        "total": total,
    }
    return render(request, 'expenses_list.html', context)


@staff_member_required
@login_required
def expenses_all(request):
    expenses = Expenses.objects.all().order_by("-timestamp")
    total = expenses.aggregate(total=Sum('amount'))['total']

    context = {
        "expenses": expenses,
        "total": total,
    }
    return render(request, 'expenses_all.html', context)


@staff_member_required
@login_required
def add_expenses(request):
    form = ExpensesForm(request.POST, request.FILES, user=request.user)
    if form.is_valid():
        form.save()
        return redirect('expenses_list')
    else:
        form = ExpensesForm(user=request.user)

    return render(request, 'add_expenses.html', {"form": form})


@login_required
def feedback_form(request):
    form = FeedbackForm(request.POST, request.FILES, user=request.user)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = FeedbackForm(user=request.user)

    return render(request, 'feedbackform.html', {"form": form})


def feedback(request):
    form = FeedbackForm2(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('feedback_sent')
    else:
        form = FeedbackForm2()
    return render(request, 'feedback.html', {"form": form})


def feedback_sent(request):
    return render(request, 'sent_feedback.html')


@staff_member_required
@login_required
def feedback_list(request):
    feedback = Feedback.objects.all().order_by("-timestamp")

    context = {
        "feedback": feedback,
    }
    return render(request, 'feedback_list.html', context)


@staff_member_required
@login_required
def rate_res(request, pk):
    query = request.GET.get('star')
    apartment = ResidentialApartment.objects.get(pk=pk)
    apartment.star = query
    apartment.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@staff_member_required
@login_required
def rate_com(request, pk):
    query = request.GET.get('star')
    apartment = CommercialApartment.objects.get(pk=pk)
    apartment.star = query
    apartment.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
