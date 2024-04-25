from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai
from django.contrib import auth #this is for the authentication system in Django
from django.contrib.auth.models import User #this is for the fetch the saved data from the saved
from django.core.mail import send_mail # for email sending
from django.conf import settings # for erciving the users email directly
from django.db import IntegrityError
from .models import Chat
from django.utils import timezone

# Create your views here.

def home(request):
    return render (request, 'home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                # Create a new user
                user = User.objects.create_user(username, email, password1)
                user.save()
                
                # Log in the user
                auth.login(request, user)

                # Send welcome email
                subject = 'PLANT-IT '
                message = ' HELLO WELCOME TO PLANT-IT'
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,  # Use your email host user as sender
                    [email],  # Send email to the user who just registered
                    fail_silently=False,
                ) 

                return redirect('home')

            except IntegrityError:
                error_message = 'User with this username or email already exists.'
                return render(request, 'register.html', {'error_message': error_message})
            except Exception as e:
                # Catch any other unexpected exceptions
                error_message = f'Error creating user: {str(e)}'
                return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = 'Password mismatch'
            return render(request,'register.html', {'error_message': error_message})
    return render(request,'register.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')