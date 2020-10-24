from django.shortcuts import render

from my_app.models import Church


def home(request):
    details = Church.objects.all()
    context = {
        'details':details
    }
    return render(request,'my_app/home.html',context)
