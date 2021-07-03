from django.shortcuts import render
from .forms import DonatePaymentForm
import razorpay
from .models import Donate

# Razorpay keys
key_id     = 'rzp_test_V0nTmLvmXrOe5z'
key_secret = 'MnhI67xm4cnaBbHQQ2v27WCd'

def donate(request):
    if request.method == "POST":
        name=request.POST.get('name')
        amount=int(request.POST.get('amount'))*100
        #create Razorpay Client
        client = razorpay.Client(auth=(key_id,key_secret))
        #create order
        response_payment = client.order.create(dict(amount=amount, currency='INR'))
        #print(response_payment)
        order_id = response_payment['id']
        order_status = response_payment['status']
        if order_status == 'created':
            Donate_x = Donate(
                name = name,
                amount = amount,
                order_id = order_id
            )
            Donate_x.save()
            response_payment['name'] = name
            

            form = DonatePaymentForm(request.POST or None)
            return render(request, 'donate/donate.html', {'form' : form,'payment' : response_payment})

    form=DonatePaymentForm()
    return render(request, 'donate/donate.html',{'form': form})

def payment_status(request):
    response = request.POST
    #print(response)
    params_dict={
        # 'razorpay_order_id'  : response['razorpay_order_id'],
        # 'razorpay_payment_id': response['razorpay_payment_id'],
        # 'razorpay_signature' : response['razorpay_signature']
        'razorpay_payment_id': response.get('razorpay_payment_id'),
        'razorpay_order_id'  : response.get('razorpay_order_id'),
        'razorpay_signature' : response.get('razorpay_signature')
    }

    #create a razorpay client instance
    client = razorpay.Client(auth=(key_id,key_secret))
    try:
        status = client.utility.verify_payment_signature(params_dict)
        Donate_x = Donate.objects.get(order_id=response['razorpay_order_id'])
        Donate_x.razorpay_payment_id = response['razorpay_payment_id']
        Donate_x.paid = True
        Donate_x.save()
        return render(request, 'donate/payment_status.html', {'status': True})
    except:
        return render(request, 'donate/payment_status.html', {'status': False})