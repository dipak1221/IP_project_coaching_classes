from django.shortcuts import render
from . models import notices,login_detail

def index(request):
    param = notices.objects.all()
    return render(request,'index.html',{'param':param})
# Create your views here.

def notice(request):
    text = request.POST.get('text')
    check = request.POST.get('check',default='off')

    n= notices.objects.all()



    if(check=='off'):
        print("pls check the check box")

    return render(request,'login.html')

def login(request):
    return render(request,'login.html')

def verify_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    param = login_detail.objects.all()

    for i in param:
        if username == i.username:
            if password == i.password:
                return render(request,'notice.html')
            else:
                print("password is incorrect ")
                return render(request,'login.html')
        else:
            print("user not exit")
            return render(request,'login.html')



    return render(request,'index.html')
