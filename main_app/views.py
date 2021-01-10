from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'main_app/index.html')

def about_us(request):
    return render(request, 'main_app/about_us.html')

def contact(request):
    return render(request, 'main_app/contact.html')

def courses(request):
    return render(request, 'main_app/courses.html')

def approvals(request):
    return render(request, 'main_app/approvals.html')

# def ad(request):
#     return render(request, 'main_app/ad.html')
