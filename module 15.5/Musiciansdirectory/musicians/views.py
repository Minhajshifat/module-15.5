from django.shortcuts import render,redirect
from . import forms

# Create your views here.
def add_musician(request):
    if request.method=='POST':
        musician_form=forms.add_musician(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('add_album')
    else:
        musician_form=forms.add_musician()
        return render(request,'add_musician.html',{'form':musician_form})