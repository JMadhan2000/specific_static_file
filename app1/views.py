from django.shortcuts import render

# Create your views here.
def static_files(request):
    return render(request,'static_files.html')