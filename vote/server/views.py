from django.http.request import HttpHeaders
from django.http import HttpResponse
from django.shortcuts import render
from .models import server, testing
event = []
# Create your views here.
choices =[]
def page1(request):
    if(request.method) == "POST":
        if request.POST.get('eventname') != "":
            if(request.POST.get("eventname")):
                 event.append(request.POST.get('eventname'))
                
            return render(request,"home.html",{
                "eventname" : request.POST.get('eventname'),
                "choices":choices
            })
        else:
            return HttpResponse("enter valid data")

    return render(request,"page1.html")

def home(request):
     
    return render(request,"home.html",{
        "choices" : choices
    })


def add(request):
    
    if request.method == "POST":
        if request.POST.get('choice'):
            if request.POST.get('[choice') != "":
                choice = request.POST.get('choice')
                choices.append(choice)



    return render(request,"add.html",{
        "temp":request.POST.get('choice')
    })



def end(request):
    ops = ['op1', 'op2', 'op3', 'op4', 'op5', 'op6', 'op7', 'op8', 'op9', 'op10']
    l_c = len(ops)
    c_c = len(choices)
    for i in range(0, c_c):
        ops[i] = choices[i]
    for i in range(c_c, l_c):
        ops[i] = "NULL"
    #################
    h = server()
    h.event = event[0]
    h.op1 = ops[0]
    h.op2 = ops[1]
    h.op3 = ops[2]
    h.op4 = ops[3]
    h.op5 = ops[4]
    h.op6 = ops[5]
    h.op7 = ops[6]
    h.op8 = ops[7]
    h.op9 = ops[8]
    h.op10 = ops[9]
    h.save()

    k = testing()
    k.test = choices
    k.save()
    chs = testing.objects.all()
    #tem = server.objects.get(event = event[0])
    return HttpResponse(server.objects.all())
    return render(request,"display.html",{
            "temp1" : tem
    })

    for k in chs:
            return render(request,"display.html",{
                "u_choices":server.objects.get(event = event[0])
            })