from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from .models import ContactMessage
from .forms import SeniorOneForm
from django.http import JsonResponse



# Create your views here.

# Mtn view
import requests
from django.conf import settings

def get_momo_token():
    url = "https://sandbox.momodeveloper.mtn.com/collection/token/" if settings.MTN_ENVIRONMENT == "sandbox" else "https://api.mtn.com/v1/oauth2/token/"
    
    headers = {
        "Authorization": f"Basic {settings.MTN_API_KEY}",
        "Ocp-Apim-Subscription-Key": settings.MTN_SUBSCRIPTION_KEY,
    }
    
    response = requests.post(url, headers=headers)
    return response.json().get("access_token")


def initiate_payment(request):
    if request.method == "POST":
        amount = request.POST.get("amount")
        phone = request.POST.get("phone")  # Format: "237699999999"
        external_id = "YOUR_UNIQUE_REFERENCE"  # e.g., order ID
        
        token = get_momo_token()
        
        url = "https://sandbox.momodeveloper.mtn.com/collection/v1_0/requesttopay" if settings.MTN_ENVIRONMENT == "sandbox" else "https://api.mtn.com/v1/requesttopay"
        
        headers = {
            "Authorization": f"Bearer {token}",
            "X-Reference-Id": external_id,
            "X-Target-Environment": settings.MTN_ENVIRONMENT,
            "Ocp-Apim-Subscription-Key": settings.MTN_SUBSCRIPTION_KEY,
            "Content-Type": "application/json",
        }
        
        payload = {
            "amount": amount,
            "currency": "UGX",  # or "USD" depending on country
            "externalId": external_id,
            "payer": {
                "partyIdType": "MSISDN",
                "partyId": phone,
            },
            "payerMessage": "Payment for service",
            "payeeNote": "Thank you!",
        }
        
        response = requests.post(url, json=payload, headers=headers)
        return JsonResponse(response.json())

    return JsonResponse({"error": "Invalid request"}, status=400)

def check_payment_status(request, transaction_id):
    token = get_momo_token()
    
    url = f"https://sandbox.momodeveloper.mtn.com/collection/v1_0/requesttopay/{transaction_id}" if settings.MTN_ENVIRONMENT == "sandbox" else f"https://api.mtn.com/v1/requesttopay/{transaction_id}"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Ocp-Apim-Subscription-Key": settings.MTN_SUBSCRIPTION_KEY,
    }
    
    response = requests.get(url, headers=headers)
    return JsonResponse(response.json())


from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def momo_callback(request):
    if request.method == "POST":
        data = request.json()
        transaction_id = data.get("financialTransactionId")
        status = data.get("status")  # SUCCESSFUL, FAILED, PENDING
        
        # Update your database here
        print(f"Payment {transaction_id} status: {status}")
        
        return HttpResponse(status=200)
    return HttpResponse(status=400)






def select_form(request):
    return render(request, 'auth/selectform.html')


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

