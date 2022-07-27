from django.shortcuts import render

# Create your views here.

def criar_conta (request):
    return render(request, 'criar_conta.html')