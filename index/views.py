from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def patient_info(request):
    return render(request, 'patient_informations.html')


def register(request):
    return render(request, 'register.html')


def chatbot(request):
    return render(request, 'chatbot.html')
