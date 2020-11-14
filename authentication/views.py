from django.shortcuts import render,redirect
from authentication.models import TableUser
#from django.http import HttpResponseRedirect



def auth_home(request):
    return render(request,"auth_home.html")


def auth_login(request):
    
        return render(request,"auth_login.html")


def auth_register(request):
    if request.method=='POST':
        #form = NameForm(request.POST)
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        mobile=request.POST['mobile']
        password=request.POST['password']

      
        enter_data=TableUser.objects.create_user(fname=fname,lname=lname,email=email,mobile=mobile,password=password)
        enter_data.save()
        print('user created .')
        return redirect('auth_login')
    else:
        return render(request,'auth_register.html')

