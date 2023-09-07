from django.shortcuts import render, redirect
from addInvoice.models import Client, Services
from addInvoice.forms import *

# Create your views here.
def addInvoice(request):

    if request.user.is_authenticated:
        try:
            if request.method == 'POST':
                clientFm = ClientForm(request.POST)
                if clientFm.is_valid():
                    
                    comp = clientFm.cleaned_data['company_name' ]
                    cntry = clientFm.cleaned_data['country']
                    sts = clientFm.cleaned_data['state']
                    add = clientFm.cleaned_data['address']
                    gst = clientFm.cleaned_data['gst_number']

                    obj = Client(company_name=comp, gst_number =gst,
                                    country=cntry, state=sts, address=add)
                    obj.save()
                        
                    clientFm = ClientForm()  
                
            else:    
                clientFm = ClientForm() 

                context = {
                    'titles':'Add Invoice - Invoice',
                    'clientFm':clientFm
                }
                 
            # if request.method == 'POST':
            #     company_name = request.POST['addClientDetailsCompanyName']
            #     gst_number = request.POST['addClientDetailsGstNumber']
            #     country = request.POST['addClientDetailsCountry']
            #     state = request.POST['addClientDetailsState']
            #     address = request.POST['addClientDetailsAddress']

            # if len(company_name)>2 and len(gst_number)==15 and len(country)>4 and len(state)>4 and len(address)>4:
            #     my_user = Client(company_name=company_name, gst_number=gst_number, country=country, state=state, address=address)
            #     my_user.save()
        except:
            pass

        return render(request, 'addInvoice/htmls/addInvoice.html', {'titles':'Add Invoice - Invoice',
                    'clientFm':clientFm})
    
    else:
        return redirect('loginPage')
    


def addInvoice2(request):

    if request.user.is_authenticated:
        try:

            if request.method == 'POST':
                serviceFm = ServicesForm(request.POST)
                if serviceFm.is_valid():
                    
                    cname = serviceFm.cleaned_data['client' ]
                    ser = serviceFm.cleaned_data['description']
                    qty = serviceFm.cleaned_data['quantity']
                    amt = serviceFm.cleaned_data['amount']
                    

                    serObj = Services(client=cname, description =ser,
                                    quantity=qty, amount=amt)
                    serObj.save()
                        
                    serviceFm = ServicesForm()  
                
            else:    
                serviceFm = ServicesForm() 
            
            # if request.method == 'POST':
            #     client = request.POST['addServiesClient']
            #     description = request.POST['addServiesDescription']
            #     quantity = request.POST['addServiesQuantity']
            #     amount = request.POST['addServiesAmount']

            # if len(description)>5 and (quantity)>0 and (amount)>=0:
            #     my_user1 = Services(client=client, description=description, quantity=quantity, amount=amount)
            #     my_user1.save()
        except:
            pass

        return render(request, 'addInvoice/htmls/addServices.html', {'titles':'Add Invoice - Invoice',
                                                                     'serviceFm':serviceFm})
    
    else:
        return redirect('loginPage')

    