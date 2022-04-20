from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import Account
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from google_auth_oauthlib.flow import  InstalledAppFlow
import pickle
def get_user(request):
        user = request.user
        user = Account.objects.get(user=user)
        return user

@login_required(login_url='signin')
def profile(request):
    user = get_user(request)
    return render(request,'myApp/blog.html',{'user':user})

def signup(request):
    if request.method == 'POST':
        type=  request.POST.get('type')
        city=  request.POST.get('city')
        state=  request.POST.get('state')
        pincode=  request.POST.get('pincode')
        image=  request.FILES['image']
        print(image)
        first_name= request.POST.get('firstName')
        last_name= request.POST.get('lastName')
        email= request.POST.get('email')
        address= request.POST.get('address')
        username= request.POST.get('username')
        password= request.POST.get('password')
        obj =User.objects.create_user(username,email,password)
        obj.first_name = first_name
        obj.last_name = last_name
        obj.save()
        account = Account.objects.create(type=type,city=city,pincode=pincode,user=obj,state=state,image=image,address=address)
        account.save()
        if type == 'doctor':
            scopes = ['https://www.googleapis.com/auth/calendar']
            flow = InstalledAppFlow.from_client_secrets_file(r'E:\rajat\Django\sign up form\blog\client.json',scopes=scopes)
            credentials = flow.run_local_server()
            pickle.dump(credentials,open(r'E:\rajat\Django\sign up form\blog\auth_token\{}_token.pkl'.format(username),'wb'))
        
        return redirect('signin')
    return render(request,'myApp/signup.html')

def signout(request):
    logout(request)
    messages.success(request,'Sign Out Successfully')
    return redirect('signin')

    
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Signed in successfully')
            return redirect('index')
        else :
            messages.error(request,'Please enter valid information')
    return render(request,'myApp/signin.html')
