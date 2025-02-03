from django.shortcuts import render

# Create your views here.

def Inicio(request):
    if request.method == "GET":
        return render(request, 'global/index.html')

