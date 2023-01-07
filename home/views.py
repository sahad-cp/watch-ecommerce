from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'f-base.html')



def watch(request):
    return render(request,'f-watches.html')



def log(request):
    return render(request,'f-log.html')