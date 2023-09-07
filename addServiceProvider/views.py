from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages

# Create your views here.

def addServiceProviderDetails(request):

    # allCompany = Company.objects.all()

    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = ServiceProviderForm(request.POST)
            if fm.is_valid():
                cnm = fm.cleaned_data['client']
                comp = fm.cleaned_data['company_name' ]
                hby = fm.cleaned_data['handle_by']
                em = fm.cleaned_data['email']
                ph = fm.cleaned_data['phone']
                acn = fm.cleaned_data['account_number']
                ifsc = fm.cleaned_data['ifsc_code']
                bname = fm.cleaned_data['bank_name']
                gst = fm.cleaned_data['gst_number']


                obj = Company(client=cnm, company_name =comp, bank_name=bname, gst_number=gst,
                                   handle_by=hby, email=em, phone=ph, account_number=acn, ifsc_code=ifsc)
                obj.save()

                fm = ServiceProviderForm()
            
        else:    
            fm = ServiceProviderForm()

        providers = Company.objects.all()
        data = {
            'titles':'Service Provider - Invoice', 
            'fm':fm,
            'providers': providers
        }
        # return render(request, 'htmls/logon.html')
        return render(request, 'addServiceProvider/htmls/addServiceProviderDetails.html', data)
    
    else:
        return redirect('loginPage')
    





def update_company(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = Company.objects.get(pk = id)
            fm = ServiceProviderForm(request.POST, instance=obj)
            if fm.is_valid():
                fm.save()
                messages.success(
                    request,"Successfully updated, you can go back"
                )
        else:
            obj = Company.objects.get(pk = id)
            fm = ServiceProviderForm(instance = obj)
        
        return render(request,'update_comp.html', {'form':fm})            
    
    else:
        return redirect('loginPage')
    
    
    
    

def delete_company(request, id):
    if request.user.is_authenticated:
        
        if request.method == 'POST':
            obj = Company.objects.get(pk=id)
            obj.delete()
        return redirect('/service_provider/')    
    
    else:
        return redirect('loginPage')