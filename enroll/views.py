
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

# Create your views here.
# this fun show and add iteams.
def add_show(request):
    if request.method == 'POST':
        sm = StudentRegistration(request.POST)
        if sm.is_valid:
            sm.save()
            sm = StudentRegistration(request.POST)
    else:
        sm = StudentRegistration()
    s = User.objects.all()

    return  render(request,'enroll/addandshow.html',{'form':sm ,'stu':s})

#this func will update the data
def update_data(request, id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
        
    return render(request,'enroll/updatestudent.html', {"form": fm})



# this func will delete the item
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')