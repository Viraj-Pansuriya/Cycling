from django.shortcuts import render
from cycle.models import CyclistModel , EventModel
from django.contrib import messages
from django.http import HttpResponse
from cycle.forms import cycforms , eveforms
from django.db import connection

def homep(request):
    return render(request , 'home.html')

def showcyc(request):
    showall=CyclistModel.objects.all()
    print(showall)
    return render(request , 'index.html' , {"data":showall})

def showeve(request):
    showall=EventModel.objects.all()
    print(showall)
    return render(request , 'index2.html' , {"data":showall})

def insertc(request):
    if request.method=="POST":
        if request.POST.get('cyclist_id') and request.POST.get('name') and request.POST.get('email_id') and request.POST.get('international_rank') and request.POST.get('national_rank') and request.POST.get('highest_speed') and request.POST.get('rating') and request.POST.get('injuries') and request.POST.get('pincode') and request.POST.get('city') and request.POST.get('state_cyl') and request.POST.get('country'):
            saverecord=CyclistModel()
            saverecord.cyclist_id=request.POST.get('cyclist_id')
            saverecord.name=request.POST.get('name')
            saverecord.email_id=request.POST.get('email_id')
            saverecord.international_rank=request.POST.get('international_rank')
            saverecord.national_rank=request.POST.get('national_rank')
            saverecord.highest_speed=request.POST.get('highest_speed')
            saverecord.rating=request.POST.get('rating')
            saverecord.injuries=request.POST.get('injuries')
            saverecord.pincode=request.POST.get('pincode')
            saverecord.city=request.POST.get('city')
            saverecord.state_cyl=request.POST.get('state_cyl')
            saverecord.country=request.POST.get('country')

            allval=CyclistModel.objects.all()
            
            for i in allval:
                if int(i.cyclist_id)==int(request.POST.get('cyclist_id')):
                    messages.warning(request,'Cyclist already exists....!');
                    return render(request,'insertcyc.html')
            
            saverecord.save()
            messages.success(request,'Cyclist '+saverecord.name+' is saved succesfully!!')
            return render(request,'insertcyc.html')
           
    else:
            return render(request,'insertcyc.html')



def inserte(request):
    if request.method=="POST":
        if request.POST.get('event_id') and request.POST.get('start_time') and request.POST.get('end_time') and request.POST.get('date') and request.POST.get('place') and request.POST.get('country') and request.POST.get('state') and request.POST.get('city') and request.POST.get('route_length') :
            saverecord=EventModel()
            saverecord.event_id=request.POST.get('event_id')
            saverecord.start_time=request.POST.get('start_time')
            saverecord.end_time=request.POST.get('end_time')
            saverecord.date=request.POST.get('date')
            saverecord.place=request.POST.get('place')
            saverecord.country=request.POST.get('country')
            saverecord.state=request.POST.get('state')
            saverecord.city=request.POST.get('city')
            saverecord.route_length=request.POST.get('route_length')
        

            allval=EventModel.objects.all()
            
            for i in allval:
                if int(i.event_id)==int(request.POST.get('event_id')):
                    messages.warning(request,'Event already exists....!');
                    return render(request,'inserteve.html')
            
            saverecord.save()
            messages.success(request,'Event '+saverecord.event_id+' is saved succesfully!!')
            return render(request,'inserteve.html')
           
    else:
            return render(request,'inserteve.html')





def editc(request ,id):
    editcobj=CyclistModel.objects.get(cyclist_id=id)
    return render(request , 'editcyc.html' , {"CyclistModel" : editcobj})


def updatec(request,id):
    updtc=CyclistModel.objects.get(cyclist_id=id)
    form=cycforms(request.POST , instance=updtc)
    if form.is_valid():
        form.save()
        messages.success(request , 'Record Updated Successfully..!')
        return render(request , 'editcyc.html' , {"CyclistModel" : updtc})



def edite(request ,id):
    editeobj=EventModel.objects.get(event_id=id)
    return render(request , 'editeve.html' , {"EventModel" : editeobj})


def updatee(request,id):
    updte=EventModel.objects.get(event_id=id)
    form=eveforms(request.POST , instance=updte)
    if form.is_valid():
        form.save()
        messages.success(request , 'Record Updated Successfully..!')
        return render(request , 'editeve.html' , {"EventModel" : updte})

def deltc(request , id):
    deltcobj=CyclistModel.objects.get(cyclist_id=id)
    deltcobj.delete()
    showall=CyclistModel.objects.all()
    return render(request,"index.html",{"data" : showall })


def delte(request , id):
    delteobj=EventModel.objects.get(event_id=id)
    delteobj.delete()
    showall=EventModel.objects.all()
    return render(request,"index2.html",{"data" : showall })


def sortc(request):
    if request.method=="POST":
        if request.POST.get('Sort'):
            type=request.POST.get('Sort')
            sorted=CyclistModel.objects.all().order_by(type)
            context = {
                'data': sorted
            }
            return render(request,'sortcyc.html',context)
    else:
        return render(request,'sortcyc.html')


def sorte(request):
    if request.method=="POST":
        if request.POST.get('Sort'):
            type=request.POST.get('Sort')
            sorted=EventModel.objects.all().order_by(type)
            context = {
                'data': sorted
            }
            return render(request,'sorteve.html',context)
    else:
        return render(request,'sorteve.html')



def runc(request):
    raw_query = "select * from cyclist where highest_speed>20;"
    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata=cursor.fetchall()
    showall=CyclistModel.objects.all()
    return render(request , "runc.html" , {"data" : alldata})


def rune(request):
    raw_query = "select * from events where event_id>40;"
    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata=cursor.fetchall()
    showall=EventModel.objects.all()
    return render(request , "rune.html" , {"data" : alldata})