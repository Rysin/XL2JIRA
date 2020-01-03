from django.http import HttpResponse
from django.shortcuts import render


def home(request):
	return HttpResponse('<h1>BraveNewWorld</h1>')


def house(request):
	return HttpResponse('<h2>IsBin</h2>')


def report(request):
	return render(request, 'quora.html')


def res(request):
	return render(request, 'htm_test.html')
