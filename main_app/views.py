from django.shortcuts import render
from django.core.mail import send_mail
from BroTathanAviation import settings

# Create your views here.

def index(request):
    if request.method == "POST":
        message_name = request.POST['name']
        message_email = request.POST['mail']
        message = request.POST['subject']

        # send Emails
        send_mail(
            'Email via Website from ' + message_name + ' ' + message_email, #subject
            message + ' Email sent from -' + message_email, #message
            message_email, #from email
            [settings.EMAIL_HOST_USER], #to email
        )
        print("sent mail")

        return render(request, 'main_app/index.html',
            {'message_name': message_name})
    else:
        return render(request, 'main_app/index.html', {})

    

def about_us(request):
    return render(request, 'main_app/about_us.html')

def contact(request):
    if request.method == "POST":
        message_name = request.POST['name']
        message_email = request.POST['mail']
        message = request.POST['subject']

        # send Emails
        send_mail(
            'Email via Website from ' + message_name + ' ' + message_email, #subject
            message + ' Email sent from -' + message_email, #message
            message_email, #from email
            [settings.EMAIL_HOST_USER], #to email
        )
        print("sent mail")

        return render(request, 'main_app/index.html',
            {'message_name': message_name})
    else:
        return render(request, 'main_app/index.html', {})

def courses(request):
    return render(request, 'main_app/courses.html')

def approvals(request):
    return render(request, 'main_app/approvals.html')

# def ad(request):
#     return render(request, 'main_app/ad.html')
