from django.http import HttpResponse
from django.shortcuts import render

from .xl2jira_script import main


def home(request):
	return HttpResponse('<h1>Welcome Homie!</h1>')


def tool_form(request):
	return render(request, 'Query.html')


def tool(request):
	keyInQuery = request.GET['KeyInQuery']
	print(keyInQuery)
	userquery = HttpResponse('<h3>' + str(keyInQuery) + '<h3>')
	br = HttpResponse('</br>')
	print('Accessing Core Tool')
	keyInResult = main(keyInQuery)
	return HttpResponse('<h2>' + keyInQuery + '</br>' + keyInResult + '</h2>')
