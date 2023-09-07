from django.shortcuts import render, HttpResponseRedirect
from authentication.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def loginPage(request):

    if not request.user.is_authenticated:

        if request.method == 'POST':
            ul = UserLogin(request=request, data=request.POST)
            if ul.is_valid():
                uname = ul.cleaned_data['username']
                upass = ul.cleaned_data['password']
                
                userObj = authenticate(username=uname, password =upass)

                if userObj is not None:
                    login(request, userObj)
                    return HttpResponseRedirect('/dashboard/')

        else:

            ul = UserLogin()

            context = {
                'titles': 'LogIn - Invoice',
                'loginForm': ul
            }

            return render(request, 'authentication/htmls/loginPage.html', context)
    
    else:
        return HttpResponseRedirect('/dashboard/')
    


def signupPage(request):

    if request.method == 'POST':
        username = request.POST['username']
        useremail = request.POST['useremail']
        userphone = request.POST['userphone']
        userstate = request.POST['userstate']
        userpassword1 = request.POST['userpassword1']
        userpassword2 = request.POST['userpassword2']

        my_user = User.objects.create_user(username, useremail, userpassword1)
        my_user.phone_number = userphone
        my_user.state = userstate
        my_user.save()
        
        messages.success(request, 'Your Account has been successfully created.')

        return HttpResponseRedirect('/')

    return render(request, 'authentication/htmls/signupPage.html', {'titles':'SignUp - Invoice'})


