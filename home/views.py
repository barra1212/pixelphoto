from django.shortcuts import render

# Create your views here.
def index(request):
    """displays index.html at home"""
    return render(request, "index.html")