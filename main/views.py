from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return HttpResponse('Wow, I am <strong>awesome!</strong>')
def home(request):
    return render(request, 'home.html')
def count(request):
    word = request.GET['text']
    length = len(word)
    return render(request, 'count.html', {'length': length, 'word':word})