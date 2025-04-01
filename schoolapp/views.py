from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from .models import ContactMessage
from .forms import SeniorOneForm


# Create your views here.
def home(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/abouthistory.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        preferred_method = request.POST.get('preferred_method')
        message = request.POST.get('message')

        # Save the message to the database
        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            preferred_method=preferred_method,
            message=message
        )

        # Configure email backend for production
        settings.EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

        # Send an email to the admin
        admin_email = "aloisiuskasozi@gmail.com"
        subject = "New Contact Message"
        email_message = f"""
        You have received a new contact message:
        Name: {name}
        Email: {email}
        Phone: {phone}
        Preferred Contact Method: {preferred_method}
        Message: {message}
        """
        send_mail(subject, email_message, settings.DEFAULT_FROM_EMAIL, [admin_email])

        # Display a success message
        messages.success(request, 'Your message has been sent successfully! You will be contacted shortly.')
        return redirect('contact')  # Replace 'contact' with the name of your contact page URL pattern

    return render(request, 'main/contact.html')

def gallery(request):
    return render(request, 'main/gallery.html')

def gamesports(request):
    return render(request, 'main/gamesports.html')

def clubsandactivities(request):
    return render(request, 'main/clubsandactivities.html')

def events(request):
    return render(request, 'main/events.html')

def schooladmin(request):
    return render(request, 'main/schooladmin.html')

def unebperformance(request):
    return render(request, 'main/unebperformance.html')

def beststudents(request):
    return render(request, 'main/beststudents.html')

def admissions(request):
    return render(request, 'main/admissions.html')



def formoneregister(request):
    if request.method == 'POST':
        form = SeniorOneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'auth/success.html')
    else:
        form = SeniorOneForm()
    return render(request, 'auth/formoneregister.html', {'form': form})

