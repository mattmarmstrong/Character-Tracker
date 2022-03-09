from multiprocessing import context

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import SheetForm


# Create your views here.

# the view used by the registration page
def regPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during')

    context = {'form': form}
    return render(request, 'base/user_registration.html', context)


# the view used by the login page
def login(request):
    # when the user attempts to login, check if they are a valid user
    if request.method == 'POST':
        username = request.POST.get('username').lower()
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

def userProfile(request, pk):
    user = User.objects.get(id = pk)
    sheets = Sheet.objects.all()
    context = {'user' : user, 'sheets': sheets}
    return render(request, 'base/profile.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')


def home(request):
    rooms = Room.objects.all()
    sheets = Sheet.objects.all()
    context = {'rooms': rooms, 'sheets': sheets}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)


def sheet(request, pk):
    sheet = Sheet.objects.get(id=pk)
    context = {'sheet': sheet}
    return render(request, 'base/sheet.html', context)


def createSheet(request):
    """
    Create sheet and save if valid.
    :param request: object to pass state to the function
    :return: url to return to
    """
    form = SheetForm()  # get default form
    if request.method == 'POST':
        form = SheetForm(request.POST)  # get form for post
        if form.is_valid():  # if valid, save, then redirect
            form.save()
            return HttpResponseRedirect('home')

    context = {'form': form}
    return render(request, 'base/sheet_form.html', context)


def updateSheet(request, pk):
    """
    Edit the sheet and saves the data if valid.
    :param request: object to pass state to the function
    :param pk: ID for the sheet
    :return: url to return to
    """
    sheet = Sheet.objects.get(id=pk)  # get sheet with ID
    form = SheetForm(instance=sheet)  # get current form

    if request.method == 'POST':
        origin = request.POST.get('origin', '/')  # get prev location to redirect
        form = SheetForm(request.POST, instance=sheet)  # get form for post
        if form.is_valid():  # if valid, save, then redirect to previous location
            form.save()
            return redirect(f'/sheet/{pk}')

    context = {'form': form}
    return render(request, 'base/sheet_form.html', context)  # otherwise don't leave


def deleteSheet(request, pk):
    """
    Delete sheet on user confirmation.
    :param request: object to pass state to the function
    :return: url to return to
    """
    sheet = Sheet.objects.get(id=pk)
    if request.method == 'POST':
        sheet.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': sheet})
