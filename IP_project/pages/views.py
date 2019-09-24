from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import HttpResponse
from . models import notices,login_detail
from django.http import HttpResponseRedirect

def index(request):
    param = list(notices.objects.all())

    param=param[:-6:-1]

    return render(request,'index.html',{'param':param})

def notice(request):
    if request.method=='POST':
        if(request.POST.get('_edit')):
            data = request.POST.get('_edit')
            print(data)

            if data[0]=='1':
                data=data[1:]
                #print(data)
                textdb=notices.objects.get(id=data)
                text=textdb.notice
                textdb.delete()
                return render(request,'notice.html',{'text':text})
            elif data[0]=='2':
                data=data[1:]
                #print(data)
                text=notices.objects.get(id=data)
                text.delete()
                par='''<script language="javascript">
                alert('Notice has been Deleted');
                </script>'''
                param = list(notices.objects.all())
                param=param[::-1]
                return render(request,'list_notice.html',{'param':param,'par': par})
    #     elif(request.POST.get('text')):
    #         text = request.POST.get('text')
    # #check = request.POST.get('check',default='off')
    # #param=''
    #
    # # if(check=='off'):
    # #     #return HttpResponse("<script>window.alert('Notice has been Submited succesfully');</script>");
    # #     print("pls check the check box")
    # #     param="Pls check the check box"
    # #     return render(request,'notice.html',{'param':param})
    #
    #         if text :
    #             n= notices(notice=text)
    #             n.save()
    #             par = '''<script language="javascript">
	# 	        alert("Notice has been updated !!");
	#         </script>'''
    #             param = list(notices.objects.all())
    #             param=param[::-1]
    #             return render(request,'list_notice.html',{'param':param,'par': par})
    #     #return HttpResponseRedirect("/list_notice/")
    #     #return render(request,'list_notice.html',{'param':param})
    #
    #     #return HttpResponse("<script>window.alert('Notice has been Submited succesfully');</script>");
    #     #return render(request,'index.html')
    #         else:
    #             return HttpResponse("<script>window.alert('Textbox  cannot be Empty');</script>");
    #     #return render(request,'index.html')

    return render(request,'notice.html')

def add_notice(request):

    text = request.POST.get('text')
    #check = request.POST.get('check',default='off')
    #param=''

    # if(check=='off'):
    #     #return HttpResponse("<script>window.alert('Notice has been Submited succesfully');</script>");
    #     print("pls check the check box")
    #     param="Pls check the check box"
    #     return render(request,'notice.html',{'param':param})

    if text :
        n= notices(notice=text)
        n.save()
        par = '''<script language="javascript">
		alert("Notice has been updated !!");
	</script>'''
        param = list(notices.objects.all())
        param=param[::-1]
        return render(request,'list_notice.html',{'param':param,'par': par})
        #return HttpResponseRedirect("/list_notice/")
        #return render(request,'list_notice.html',{'param':param})

        #return HttpResponse("<script>window.alert('Notice has been Submited succesfully');</script>");
        #return render(request,'index.html')
    else:
        return HttpResponse("<script>window.alert('Textbox  cannot be Empty');</script>");
        #return render(request,'index.html')

def list_notice(request):
    param = list(notices.objects.all())
    param=param[::-1]

    #print("list_notice",param)
    return render(request,"list_notice.html",{'param':param})

# def modify_notice(request):
#     data = request.POST.get('_edit')
#     print(data)
#
#     if data[0]=='1':
#         data=data[1:]
#         #print(data)
#         text=notices.objects.get(id=data)
#         text=text.notice
#         return render(request,'notice.html',{'text':text})
#     elif data[0]=='2':
#         data=data[1:]
#         #print(data)
#         text=notices.objects.get(id=data)
#         text.delete()
#         par='''<script language="javascript">
#         alert('Notice has been Deleted');
#         # </script>'''
#         param = list(notices.objects.all())
#         param=param[::-1]
#         return render(request,'list_notice.html',{'param':param,'par': par})

        #return HttpResponseRedirect('/list_notice/')
        #return render_to_response('list_notice.html', {'param':param,'par': par})
        #return render(request,'list_notice.html',{'par':par})


def expand_notice(request):
    param = list(notices.objects.all())
    param=param[::-1]
    print(param)
    return render(request,"expand_notice.html",{'param':param})


def login(request):
    return render(request,'login.html')

def verify_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    param = login_detail.objects.all()

    for i in param:
        if username == i.username:
            if password == i.password:
                return HttpResponseRedirect('/list_notice/')
                #par=''
                #return list_notice(request,par)
            else:
                print("password is incorrect ")
                return render(request,'login.html')
        else:
            print("user not exit")
            return render(request,'login.html')



    return render(request,'index.html')
