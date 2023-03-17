from django.shortcuts import render

# Create your views here.
def guitar(request):
    return render(request,'guitar.html')