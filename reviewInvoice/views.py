from django.shortcuts import render,redirect
from reviewInvoice.models import *

# Create your views here.
def allClientDetails(request):
    
    if request.user.is_authenticated:
        allClientDetails = Client.objects.all() 
        return render(request, 'reviewInvoice/htmls/allClientDetails.html', {'allclients':allClientDetails, 'titles':'Review Invoice - Invoice'})
    
    else:
        return redirect('loginPage')




def showReview(request, pk):
    if request.user.is_authenticated:
        clientData = Client.objects.get(id=pk)

        try:
            companyData = Company.objects.get(client_id=pk)
        except Company.DoesNotExist:
            companyData = {'key':'val'}

        try:
            servicesData = Services.objects.filter(client_id=pk)
        except Services.DoesNotExist:
            servicesData = {'key':'val'}

        context = {
            'clientData':clientData,
            'companyData':companyData,
            'servicesData':servicesData,
            'titles':'Review Invoice - Invoice'
        }


        return render(request, 'reviewInvoice/htmls/showReview.html', context)
    
    else:
        return redirect('loginPage')