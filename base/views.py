from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm
import requests
from django.contrib.auth import login, logout, authenticate


def register(request):
    url = requests.get('https://gerador-nomes.herokuapp.com/nome/aleatorio')
    req = url.json()
    name_api = ' '.join(req[0::])

    api_dict = {'name': name_api}

    form = PersonForm(request.POST or None, initial=api_dict)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('list')

    context = {'form': form, 'name_api': name_api}
    return render(request, 'base/home.html', context)


def listPerson(request):
    persons = Person.objects.all()

    context = {'persons': persons}
    return render(request, 'base/list.html', context)


def viewPerson(request, pk):
    person = Person.objects.get(id=pk)

    context = {'person': person}
    return render(request, 'base/view.html', context)


def editPerson(request, pk):
    person = Person.objects.get(id=pk)
    form = PersonForm(instance=person)

    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('list')

    context = {'person': person, 'form': form}
    return render(request, 'base/edit.html', context)


def deletePerson(request, pk):
    person = Person.objects.get(id=pk)

    if request.method == 'POST':
        person.delete()
        return redirect('list')

    context = {'person': person}
    return render(request, 'base/delete.html', context)
