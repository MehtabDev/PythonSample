from django.shortcuts import render

def home(request):
    return render(request, 'mehtabsite/home.html')

def about(request):
    return render(request, 'mehtabsite/about.html')

def courses(request):
    return render(request,'mehtabsite/courses.html')

def mobiles(request):
    return render(request,'mehtabsite/mobiles.html')