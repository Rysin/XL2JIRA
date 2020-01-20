from django.http import HttpResponse
from django.shortcuts import render

from .xl2jira_script import keyin


def home(request):
	return HttpResponse('<h1>Welcome Homie!</h1>')


def tool_form(request):
	return render(request, 'Query.html')


def tool(request):
	keyInQuery = request.GET['KeyInQuery']
	keyInResult = keyin(keyInQuery)
	return render(request, 'Result.html', {'result': keyInResult, 'query': keyInQuery})
