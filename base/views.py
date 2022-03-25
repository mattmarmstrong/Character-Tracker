from multiprocessing import context

from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as dj_login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView

from .models import *
from .forms import SheetForm, RateForm


# Create your views here.

# the view used by the registration page
def reg_page(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            dj_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during')

    context = {'form': form}
    return render(request, 'base/user_registration.html', context)


# the view used by the login page
def login(request):
    # when the user attempts to login, check if they are a valid user
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check if the user does exits
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        # validate the user login information
        user = authenticate(request, username=username, password=password)

        # if the user is not None, then login the user and redirect
        # them to the home page
        if user is not None:
            dj_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password are not recognized')

    context = {}
    return render(request, 'base/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


@login_required(login_url='/login')
def user_profile(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    search = q.split(";")
    sheets = Sheet.objects.filter(name__icontains=q)
    found = ''

    if ";" in q:
        if "name" in search[0]:
            sheets = Sheet.objects.filter(name__icontains=search[1].strip())
        elif "level" in search[0]:
            if search[1].strip().isnumeric():
                sheets = Sheet.objects.filter(lvl=search[1].strip())
        elif "class" in search[0]:
            sheets = Sheet.objects.filter(classes__icontains=search[1].strip())
        elif "date" in search[0]:
            sheets = Sheet.objects.filter(created__icontains=search[1].strip())

    if not sheets.exists():
        if ";" in q:
            found = f"{search[0].capitalize()}: {search[1]} was not found!"

    context = {'sheets': sheets, 'found': found}
    return render(request, 'base/profile.html', context)


@login_required(login_url='/login')
def home(request):
    return render(request, 'base/home.html')


@login_required(login_url='/login')
def glossary(request):
    return render(request, 'base/glossary.html')


@login_required(login_url='/login')
def rate_options(request):
    ratings = Rating.objects.all()
    feats = Feat.objects.all()

    context = {'ratings': ratings, 'feats': feats}
    return render(request, 'base/rate_options.html', context)


@login_required(login_url='/login')
def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)


@login_required(login_url='/login')
def feat(request, pk):
    feat = Feat.objects.get(id=pk)
    context = {'feat': feat}
    return render(request, 'base/feat.html', context)


@login_required(login_url='/login')
def sheet(request, pk):
    sheet = Sheet.objects.get(id=pk)

    if request.user != sheet.user and not request.user.is_superuser:  # only admins or users can view their own sheets
        return redirect('home')

    feats = sheet.feats.all()

    context = {'sheet': sheet, 'feats': feats}
    return render(request, 'base/sheet.html', context)


@login_required(login_url='/login')  # can only be used by users that are logged in, else redirect to login page
def create_sheet(request):
    """
    Create sheet and save if valid.
    :param request: object to pass state to the function
    :return: url to redirect the user to
    """
    form = SheetForm()  # get default form

    if request.method == 'POST':
        form = SheetForm(request.POST)  # get form for post
        if form.is_valid():  # if valid, save, then redirect
            form = form.save(commit=False)  # save the form, then update user to user who created the sheet
            form.user = request.user
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/sheet_form.html', context)


@login_required(login_url='/login')  # can only be used by users that are logged in, else redirect to login page
def update_sheet(request, pk):
    """
    Edit the sheet and saves the data if valid.
    :param request: object to pass state to the function
    :param pk: ID for the sheet
    :return: url to redirect the user to
    """
    sheet = Sheet.objects.get(id=pk)  # get sheet with ID
    form = SheetForm(instance=sheet)  # get current form

    if request.user != sheet.user and not request.user.is_superuser:  # only admins or users can edit their own sheets
        return redirect('home')

    if request.method == 'POST':
        form = SheetForm(request.POST, instance=sheet)  # get form for post
        if form.is_valid():  # if valid, save, then redirect to previous location
            form.save()
            return redirect(f'/sheet/{pk}')

    context = {'form': form}
    return render(request, 'base/sheet_form.html', context)  # render existing form


@login_required(login_url='/login')  # can only be used by users that are logged in, else redirect to login page
def delete_sheet(request, pk):
    """
    Delete sheet on user confirmation.
    :param request: object to pass state to the function
    :return: url to redirect the user to
    """
    sheet = Sheet.objects.get(id=pk)

    if request.user != sheet.user and not request.user.is_superuser:  # only admins or users can delete their own sheets
        return redirect('home')

    if request.method == 'POST':
        sheet.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': sheet})


@login_required(login_url='/login')
def rate(request, pk):
    feat = Feat.objects.get(id=pk)
    user = request.user

    form = RateForm()

    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = user
            rate.feat = feat
            alreadyRated = Rating.objects.filter(user=user).filter(feat=feat)
            if alreadyRated:
                alreadyRated.delete()
            rate.save()
            return redirect(f'/feat/{pk}')

    return render(request, 'base/rate.html', {'form': form, 'feat': feat})
