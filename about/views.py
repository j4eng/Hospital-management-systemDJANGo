from django.shortcuts import render,HttpResponse,redirect
#from .models import MyModel
#from .forms import MyForm
# Create your views here.
def about(request):
   #return HttpResponse("hiiiiiii")
    return render (request,'about.html')
