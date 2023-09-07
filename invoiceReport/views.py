from django.shortcuts import render, redirect
from invoiceReport.models import *

# Create your views here.
def invoiceReport(request):

    if request.user.is_authenticated:
        allClientDetails = Client.objects.all() 
        context = {
            'titles':'Invoice Report - Invoice',
            'allclients':allClientDetails,
        }

        return render(request, 'invoiceReport/htmls/invoiceReport.html', context)
    
    else:
        return redirect('loginPage')
    

def gstReport(request,pk):
    if request.user.is_authenticated:
        gstClientData = Client.objects.get(id=pk)

        context = {
            'gstClientData':gstClientData,
            'titles':'Invoice Report - Invoice',
        } 
        return render(request, 'invoiceReport/htmls/gstReport.html', context)    

    else:
        return redirect('loginPage')   