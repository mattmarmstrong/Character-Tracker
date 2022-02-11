from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from .forms import SheetForm

# Create your views here.

def regPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User does not exit')

    context = {}
    return render(request, 'base/user_registration.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User does not exit')

    context = {}
    return render(request, 'base/user_registration.html', context)

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
    form = SheetForm()
    if request.method == 'POST':
        form = SheetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/sheet_form.html', context)


def updateSheet(request, pk):
    sheet = Sheet.objects.get(id=pk)
    form = SheetForm(initial=sheet)

    if request.method == 'POST':
        form = SheetForm(request.POST, instance=sheet)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {}
    return render(request, 'base/sheet_form.html', context)


def deleteSheet(request, pk):
    sheet = Sheet.objects.get(id=pk)
    if request.method == 'POST':
        sheet.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': sheet})