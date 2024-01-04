from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def add_album(request):
     if request.method == 'POST':
       album_form = forms.add_album(request.POST)
       if album_form.is_valid():
        album_form.save()
        return redirect('add_album')
    
     else:
        album_form = forms.add_album()
     return render(request, 'add_album.html', {'form' : album_form})

def edit_post(request,id):
   post=models.album.objects.get(pk=id)
   album_form = forms.add_album(instance=post)
   if request.method == 'POST':
       album_form = forms.add_album(request.POST,instance=post)
       if album_form.is_valid():
        album_form.save()
        return redirect('home')
    
   return render(request, 'add_album.html', {'form' : album_form})
def delete_post(request, id):
    post = models.album.objects.get(pk=id) 
    post.delete()
    return redirect('home')