from django.shortcuts import render,HttpResponse,redirect
#from .models import MyModel
#from .forms import MyForm
# Create your views here.
def home(request):
   #return HttpResponse("hiiiiiii")
    return render (request,'home.html')

      
