# payments/views.py
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from requests_oauthlib import OAuth1Session

CONSUMER_KEY = '9M7BoVtiphpimIDLuAS3Ww9RQOzJC/IG'
CONSUMER_SECRET = 'A1zWULNfoA+8wnjTLXznksR7iTI='
CALLBACK_URL = 'http://127.0.0.1:8000/payment/confirmation/'  # Change for production

def payment_page(request):
    return render(request, 'pay.html')

def initiate_payment(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        reference = "ORDER-" + phone[-4:]

        payload = {
            "Amount": amount,
            "Description": "Payment for services",
            "Type": "MERCHANT",
            "Reference": reference,
            "Email": email,
            "PhoneNumber": phone,
            "Currency": "UGX",
            "CallbackURL": CALLBACK_URL,
        }

        oauth = OAuth1Session(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
        response = oauth.post("https://cybqa.pesapal.com/pesapalv3/api/PostPesapalDirectOrderV4", json=payload)

        print("Raw response status:", response.status_code)
        print("Raw response text:", response.text)  # 👈 THIS will show what Pesapal returned

        try:
            data = response.json()
            redirect_url = data.get('redirect_url')
            return redirect(redirect_url)
        except Exception as e:
            return HttpResponse(f"Error decoding response: {e}\n{response.text}", status=500)

@csrf_exempt
def payment_confirmation(request):
    if request.method == 'POST':
        # Here you can verify the transaction status with Pesapal
        return HttpResponse("Confirmation received")
    return HttpResponse("Invalid", status=400)
