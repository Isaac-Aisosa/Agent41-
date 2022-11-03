from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .form import *
from .models import *
from Apartments.models import *


# Create your views here.
def landlord_signup(request):
    if request.method == 'POST':
        form = LL_SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('landlord_profile')
    else:
        form = LL_SignUpForm()

    context = {

        'form': form,

    }
    return render(request, 'Landlord_signup.html', context)


@login_required
def create_landlord_profile(request):
    form = LandlordProfilesForm(request.POST, request.FILES, user=request.user)
    if form.is_valid():
        instance = form.save()
        profile = UserProfiles.objects.get(pk=instance.pk)
        profile.landlord = True
        profile.agent = False
        profile.staff = False
        profile.admin = False
        profile.save()
        return redirect('landlord_index')
    else:
        form = LandlordProfilesForm(user=request.user)

    return render(request, 'LandlordProfiles.html', {"form": form, })


def landlord_index(request):
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
        return render(request, "landlord_index.html", context)
    else:
        return redirect('landlord_login')


def landlord_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('landlord_index')

    return render(request, 'landlord_login.html ')


@login_required
def landlord_apartment_details(request, pk):
    user = request.user
    profile = UserProfiles.objects.get(user=user)
    apartment = ResidentialApartment.objects.get(pk=pk)
    context = {
        "profile": profile,
        "apartment": apartment,
    }
    return render(request, "landlord_apartment_details.html", context)


@login_required
def landlord_commercial_apartment_details(request, pk):
    user = request.user
    profile = UserProfiles.objects.get(user=user)
    apartment = CommercialApartment.objects.get(pk=pk)
    context = {
        "profile": profile,
        "apartment": apartment,
    }
    return render(request, "landlord_commercial_apartment_details.html", context)


def landlord_profile(request):
    if request.user.is_authenticated:
        user = request.user
        profile = UserProfiles.objects.get(user=user)
        context = {
            "profile": profile,

        }
        return render(request, "landlord_profile.html", context)
    else:
        return redirect('landlord_login')


@login_required
def edit_landlord_profile(request):
    user = get_object_or_404(UserProfiles, user=request.user)
    landlord_edit_form = LandlordProfilesEditForm(instance=user)
    if request.method == "POST":
        landlord_edit_form = LandlordProfilesEditForm(request.POST, request.FILES, instance=user)
        if landlord_edit_form.is_valid():
            landlord_edit_form.save()
            return redirect('landlord_profile2')

    context = {'form': landlord_edit_form}

    return render(request, 'edit_landlord_profile.html', context)
