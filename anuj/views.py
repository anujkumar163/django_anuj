from django.shortcuts import render
 
def basic(request):
 	name = "Anuj Kumar"
 	return render(request, "indix.html", {'data': name} )