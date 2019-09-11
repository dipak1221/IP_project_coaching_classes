from django.shortcuts import render
from django.http import HttpResponse
from . models import notices,login_detail

def index(request):
    param = notices.objects.all()

    #reversed(sorted(param.keys()))
    print(param.values())
    return render(request,'index.html',{'param':param})
# Create your views here.

def notice(request):
    text = request.POST.get('text')
    check = request.POST.get('check',default='off')


    if(check=='off'):
        print("pls check the check box")
        return render(request,'notice.html')



    if text :
        n= notices(notice=text)
        n.save()
        return HttpResponse("<script>window.alert('Notice has been Submited succesfully');</script>");
        #pass
        #return render(request,'index.html')

    else:
        return HttpResponse("<script>window.alert('Text cannot be Empty');</script>");
        #return render(request,'index.html')


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
