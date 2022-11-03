from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from Management.models import Agent41Details
from User_Profiles.models import UserProfiles
from .forms import ResidentialApartmentForm, CommercialApartmentForm
from .models import *
from django.views.generic.list import ListView

from itertools import chain


# Create your views here.


def index(request):
    details = Agent41Details.objects.get(pk=1)
    context = {
        'details': details,
    }
    return render(request, 'index.html', context)


def select_type(request):
    context = {

    }
    return render(request, 'select_type.html', context)


def residential_details(request, pk):
    apartment = ResidentialApartment.objects.get(pk=pk)
    details = Agent41Details.objects.get(pk=1)

    context = {
        "apartment": apartment,
        'details': details,
    }
    return render(request, 'residential_details.html', context)


def commercial_details(request, pk):
    apartment = CommercialApartment.objects.get(pk=pk)
    details = Agent41Details.objects.get(pk=1)
    context = {
        "apartment": apartment,
        'details': details,
    }
    return render(request, 'commercial_details.html', context)


def search_residential(request):
    details = Agent41Details.objects.get(pk=1)
    query = request.GET.get('resident')
    if query is not None:
        lookups = Q(name__icontains=query) | Q(price__icontains=query) | Q(power__icontains=query) | \
                  Q(location__location__icontains=query) | Q(type__type__icontains=query) | Q(water__icontains=query) | \
                  Q(city__city__icontains=query) | Q(state__state__icontains=query) | Q(power__icontains=query)

        apartment = ResidentialApartment.objects.filter(lookups).distinct()

        context = {
            'apartment': apartment,
            'query': query,
            'details': details,

        }
        return render(request, 'search_residential.html', context)


def search_commercial(request):
    details = Agent41Details.objects.get(pk=1)
    query = request.GET.get('commercial')
    if query is not None:
        lookups = Q(name__icontains=query) | Q(price__icontains=query) | Q(power__icontains=query) | \
                  Q(location__location__icontains=query) | Q(type__type__icontains=query) | \
                  Q(city__city__icontains=query) | Q(state__state__icontains=query) | Q(power__icontains=query)

        apartment = CommercialApartment.objects.filter(lookups).distinct()

        context = {
            'apartment': apartment,
            'query': query,
            'details': details,

        }
        return render(request, 'search_commercial.html', context)


def filter_commercial(request):
    details = Agent41Details.objects.get(pk=1)
    types = request.GET.get('type')
    location = request.GET.get('location')
    power = request.GET.get('power')
    min_price = request.GET.get('min')
    max_price = request.GET.get('max')

    typess = CommercialApartment.objects.filter(type__type__iexact=types)
    locations = CommercialApartment.objects.filter(location__location__iexact=location)
    min_prices = CommercialApartment.objects.filter(price__iexact=min_price)
    max_prices = CommercialApartment.objects.filter(price__iexact=max_price)
    combined_results = list(chain(typess, locations, max_prices, min_prices))

    context = {
        'combined_results': combined_results,
        'details': details,

    }
    return render(request, 'filter_commercial.html', context)


def filter_residential(request):
    details = Agent41Details.objects.get(pk=1)
    types = request.GET.get('type')
    location = request.GET.get('location')
    power = request.GET.get('power')
    water = request.GET.get('water')
    min_price = request.GET.get('min')
    max_price = request.GET.get('max')

    typess = ResidentialApartment.objects.filter(type__type__iexact=types)
    locations = ResidentialApartment.objects.filter(location__location__iexact=location)
    min_prices = ResidentialApartment.objects.filter(price__iexact=min_price)
    max_prices = ResidentialApartment.objects.filter(price__iexact=max_price)
    combined_results = list(chain(typess, locations, max_prices, min_prices))

    context = {
        'combined_results': combined_results,
        'details': details,

    }
    return render(request, 'filter_residential.html', context)


class Residential(ListView):
    model = ResidentialApartment
    paginate_by = 3
    context_object_name = 'apartment'
    template_name = 'residential.html'

    def get_context_data(self, **kwargs):
        context = super(Residential, self).get_context_data(**kwargs)
        context.update({
            'type': ApartmentType.objects.all(),
            'location': Location.objects.all(),
            "details": Agent41Details.objects.get(pk=1),
            'power': POWER,
            'water': WATER,
        })
        return context

    def get_queryset(self):
        return ResidentialApartment.objects.filter(approved=True, unapproved=False).order_by("-star")


class Commercial(ListView):
    model = CommercialApartment
    paginate_by = 3
    context_object_name = 'apartment'
    template_name = 'commercial.html'

    def get_context_data(self, **kwargs):
        context = super(Commercial, self).get_context_data(**kwargs)
        context.update({
            "details": Agent41Details.objects.get(pk=1),
            'type': ApartmentTypeCommercial.objects.all(),
            'location': Location.objects.all(),
            'power': POWER,
        })
        return context

    def get_queryset(self):
        return CommercialApartment.objects.filter(approved=True, unapproved=False).order_by("-star")


def residential_apartment_request(request, pk):
    apartment = ResidentialApartment.objects.get(pk=pk)
    context = {
        "apartment": apartment,
    }
    return render(request, 'residential_apartment_request.html', context)


def commercial_apartment_request(request, pk):
    apartment = CommercialApartment.objects.get(pk=pk)
    context = {
        "apartment": apartment,
    }
    return render(request, 'commercial_apartment_request.html', context)


def get_residential_apartment(request):
    name = request.GET.get('name')
    phone = request.GET.get('phone')
    apartment = request.GET.get('apartment')
    ap = ResidentialApartment.objects.get(pk=apartment)
    newRequest = ResidentialApartmentRequest()
    newRequest.client = name
    newRequest.phone = phone
    newRequest.apartment = ap
    newRequest.save()
    agent41_details = Agent41Details.objects.get(pk=1)
    context = {
        "agent41_details": agent41_details,
    }
    return render(request, 'request_success.html', context)


def get_commercial_apartment(request):
    name = request.GET.get('name')
    phone = request.GET.get('phone')
    apartment = request.GET.get('apartment')
    ap = CommercialApartment.objects.get(pk=apartment)
    newRequest = CommercialApartmentRequest()
    newRequest.client = name
    newRequest.phone = phone
    newRequest.apartment = ap
    newRequest.save()
    agent41_details = Agent41Details.objects.get(pk=1)
    context = {
        "agent41_details": agent41_details,
    }
    return render(request, 'request_success.html', context)


def confirm_apartment(request, pk):
    user = request.user
    request = ResidentialApartmentRequest.objects.get(pk=pk)
    request.user = user
    request.comfirmed = True
    request.save()
    return redirect('management_res_apartment_request')


def confirm_apartment_comm(request, pk):
    user = request.user
    request = CommercialApartmentRequest.objects.get(pk=pk)
    request.user = user
    request.comfirmed = True
    request.save()
    return redirect('management_res_apartment_request')


def approve_res_apartment(request, pk):
    user = request.user
    apartment = ResidentialApartment.objects.get(pk=pk)
    apartment.approved_by = user
    apartment.approved = True
    apartment.unapproved = False
    apartment.save()
    users = apartment.user
    profile = UserProfiles.objects.get(user=users)
    profile.apartment += 1
    profile.save()
    return redirect('management_apartment_pending')


def approve_comm_apartment(request, pk):
    user = request.user
    apartment = CommercialApartment.objects.get(pk=pk)
    apartment.approved_by = user
    apartment.approved = True
    apartment.unapproved = False
    apartment.save()
    users = apartment.user
    profile = UserProfiles.objects.get(user=users)
    profile.apartment += 1
    profile.save()
    return redirect('management_apartment_pending')


def unapprove_res_apartment(request, pk):
    user = request.user
    apartment = ResidentialApartment.objects.get(pk=pk)
    apartment.approved_by = user
    apartment.approved = False
    apartment.unapproved = True
    apartment.save()
    return redirect('management_apartment_pending')


def unapprove_comm_apartment(request, pk):
    user = request.user
    apartment = CommercialApartment.objects.get(pk=pk)
    apartment.approved_by = user
    apartment.approved = False
    apartment.unapproved = True
    apartment.save()
    return redirect('management_apartment_pending')


@login_required
def select_form(request):
    context = {

    }
    return render(request, 'select_form.html', context)


@login_required
def residential_apartment_form(request):
    form = ResidentialApartmentForm(request.POST, request.FILES, user=request.user)
    if form.is_valid():
        form.save()
        return redirect('landlord_index')
    else:
        form = ResidentialApartmentForm(user=request.user)
    return render(request, 'residential_apartment_form.html', {"form": form, })


@login_required
def commercial_apartment_form(request):
    form = CommercialApartmentForm(request.POST, request.FILES, user=request.user)
    if form.is_valid():
        form.save()
        return redirect('landlord_index')
    else:
        form = CommercialApartmentForm(user=request.user)
    return render(request, 'commercial_apartment_form.html', {"form": form, })
