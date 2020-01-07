from django.shortcuts import render
from enqapp.models import ENQdata
from enqapp.forms import Forms
from django.http.response import HttpResponse

def EnqView(request):
    if request.method=="POST":
        ef=Forms(request.POST)
        if ef.is_valid():
            N1=request.POST.get('name')
            N2=request.POST.get('mobile')
            N3=request.POST.get('email')
            N4=ef.cleaned_data.get('course')
            N5=ef.cleaned_data.get('teacher')
            N6=ef.cleaned_data.get('braches')
            N7=ef.cleaned_data.get('gender')
            N8=ef.cleaned_data.get('start_date')

            data=ENQdata(
                name=N1,
                mobile=N2,
                email=N3,
                course=N4,
                teacher=N5,
                braches=N6,
                gender=N7,
                start_date=N8
            )
            data.save()
            ef = Forms()
            return render(request, 'home.html', {"asd": ef})

        else:
            return HttpResponse(" yours missed")
    else:
        ef=Forms()
        return render(request,'home.html',{"asd":ef})

