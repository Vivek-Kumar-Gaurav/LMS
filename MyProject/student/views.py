from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from user.models import *

# Create your views here.

def index(request):
    return render(request,'student/index.html')

def batches(request):
    batchdata = newbatches.objects.all().order_by('-id')
    md = {"bdata": batchdata}
    return render(request,'student/batches.html',md)

def lectures(request):
    cdata=category.objects.all().order_by('-id')
    md={"cdata":cdata}
    return render(request,'student/lectures.html',md)

def lecturesvideo(request):
    batchid=request.session.get('batchid')
    cid=request.GET.get('cid')
    vdata=mylectures.objects.filter(video_category=cid,video_batch=batchid)
    md={"vdata":vdata}
    return render(request,'student/lecturesvideo.html',md)

def liveclasses(request):
    batchid=request.session.get('batchid')
    data=batchtiming.objects.filter(batch=batchid)
    md={"data":data}
    return render(request,'student/liveclasses.html',md)

def logout(request):
    user=request.session.get('user')
    if user:
        del request.session['user']
        del request.session['userpic']
        del request.session['username']
        return HttpResponse("<script>location.href='/user/index/'</script>")
    return render(request,'student/logout.html')
def notes(request):
    bid=request.session.get('batchid')
    #print(bid)
    ndata=enotes.objects.filter(batch=bid)
    md={"ndata":ndata}
    return render(request,'student/notes.html',md)

def softwarekit(request):
    x=mysoftware.objects.all().order_by('-id')
    md={"sdata":x}
    return render(request,'student/softwarekit.html',md)

def tasks(request):
    return render(request,'student/tasks.html')

def uprofile(request):
    user=request.session.get('user')
    udata=signup.objects.filter(email=user)
    md={"udata":udata}
    if request.method=="POST":
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        passwd=request.POST.get('passwd')
        college=request.POST.get('college')
        course=request.POST.get('course')
        picture=request.FILES['fu']
        signup(name=name,mobile=mobile,passwd=passwd,college=college,course=course,
               profile=picture,email=user).save()
        return HttpResponse("<script>alert('Your profile is updated successfully..');"
                            "location.href='/student/uprofile/'</script>")

    return render(request,'student/uprofile.html',md)

