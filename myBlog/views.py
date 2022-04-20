import pickle
from unicodedata import category
from googleapiclient.discovery import build
from django.shortcuts import redirect, render
from .models import Post,Appointment
from myApp.models import Account
from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime,timedelta
def get_user(request):
        user = request.user
        user = Account.objects.filter(user=user)
        if len(user)>0:
            return user[0]
        
        else :
            return None
        


def index(request):
    category = Post.objects.values('category')
    posts_dict = {}
    if  request.user.is_authenticated:
        user = get_user(request)
        if user == None:
            return redirect('signin')
    else:
        return redirect('signin')
    for i in category:
        posts = Post.objects.filter(category=i['category'],is_draft='false')
        if len(list(posts)) > 0:
            posts_dict[i['category']] = posts 

    return render(request , 'myBlog/myPost.html',{'posts' : posts_dict,'user':user,'is_all_post':True})


def create_post(request):
    account = get_user(request)
    post_cat = ['mental health','heart disease','covid19','immunization']
    if request.method == 'POST' and request.user.is_authenticated:
        if account.type == 'doctor':
            
            category= request.POST['category']
            title= request.POST['title']
            content= request.POST['content']
            summary= request.POST['summary']
            image = request.FILES['image']
            draft = request.POST.get('draft','off')

            if draft == 'on':
                draft = 'true'
            else :
                draft = 'false'
            Post.objects.create(title=title,category=category,content=content,summary=summary,image=image,is_draft=draft,user=account)
            messages.success(request,'Post Created Successfully')
            return redirect('my_posts')
    return render(request,'myBlog/createPost.html',{'user':account,'post_cat':post_cat})


def my_posts(request):
    category = Post.objects.values('category')
    my_posts_dict = {}
    user = get_user(request)
    for i in category:
        posts = Post.objects.filter(category=i['category'],user=user)
        if len(posts) >0:
            my_posts_dict[i['category']] =posts     

    return render(request , 'myBlog/myPost.html',{'posts' : my_posts_dict,'user':user})

def blog_no(request,id):
    post = Post.objects.filter(id=id)[0]

    return render(request,'myBlog/blog.html',{'user':get_user(request),'post':post})
    
def un_draft(request,id):
    post = Post.objects.get(id=id)
    post.is_draft = 'false'
    post.save()
    messages.success(request,'Post Unmarked As Draft')
    return redirect('my_posts')

def doctors(request):
    doctors = Account.objects.filter(type='doctor')
    if request.method == 'POST':
        doctor = request.POST['doctor']
        return render(request,'myBlog/book_appointment.html',{'doctor':doctor,'user':get_user(request),'doctors':doctors})
    return render(request,'myBlog/doctors.html',{'doctors':doctors,'user':get_user(request)})


def book_apmt(request):
    user = get_user(request)
    doctors = Account.objects.filter(type='doctor')
    if  request.user.is_authenticated  and request.method == 'POST':
        username=request.POST['username']
        date=request.POST['date']
        time=request.POST['time']
        cat=request.POST['cat']
        date_time = date+' '+time
        date_time=datetime.strptime(date_time, r'%Y-%m-%d %H:%M')
        end_time = date_time+timedelta(minutes=45)
        endTime =end_time.strftime(r'%Y-%m-%dT%H:%M:%S')
        dateTime = date_time.strftime(r'%Y-%m-%dT%H:%M:%S')
        timezone = 'Asia/Kolkata'
        credentials = pickle.load(open(r'E:\rajat\Django\sign up form\blog\auth_token\{}_token.pkl'.format(username),'rb'))
        service = build('calendar','v3',credentials=credentials)
        Appointment.objects.create(doctor=username,user=user,category=cat,time=date_time,end_time=end_time)
        
        event = {
                'summary': f'Appointment With {user.user}',
                'description': f'Appointment Scheduled With {user.user} About {cat}',
                'start': {
                    'dateTime': dateTime,
                    'timeZone': timezone,
                },
                'end': {
                    'dateTime': endTime,
                    'timeZone': timezone,
                },
                }

        event = service.events().insert(calendarId='primary', body=event).execute()
        return redirect('my_apmt')
    return render(request,'myBlog/book_appointment.html',{'user':user,'doctors':doctors,'doctor':None})

def my_apmt(request):
    user = get_user(request)
    appointments = Appointment.objects.filter(user=user)
    apmts = []
    if len(appointments ) > 0:
        is_apmts=True
        for i in appointments:
            doctor = User.objects.filter(username=i.doctor)
            if len(doctor)>0:
                doctor = Account.objects.filter(user=doctor[0])[0]
                apmts.append({'apmt':i,'doctor':doctor})
    else :
        is_apmts = False

    return render(request,'myBlog/my_appointment.html',{'user':user,'apmts':apmts,'is_apmts':is_apmts})
