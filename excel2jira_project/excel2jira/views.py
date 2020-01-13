from django.http import HttpResponse
from django.shortcuts import render

from .xl2jira_script import main


def home(request):
	return HttpResponse('<h1>Welcome Homie!</h1>')


def tool(request):
	print('Accessing Core Tool')
	keyInResult = main()
	return HttpResponse('<h2>' + str(keyInResult) + '</h2>')


def tool_form(request):
	return render(request, 'Query.html')
