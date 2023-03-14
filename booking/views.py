from django.shortcuts import render,HttpResponse,redirect
from django.shortcuts import render
from .models import booking
from .forms import BookForm
# Create your views here.


def my_form(request):
  if request.method == "POST":
    form = BookForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = BookForm()
  return render(request, 'booking.html', {'form': form})