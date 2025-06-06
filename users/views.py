from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm

def register(response):
    form=UserCreationForm()
    if response.method == 'POST':
        form=UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('item_list')
    else:
        form=UserCreationForm()
    return render(response,'registration/register.html',{'form':form})
