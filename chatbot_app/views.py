from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.
def hi(request):
    return render(request, 'chatbot_app/index.html')
