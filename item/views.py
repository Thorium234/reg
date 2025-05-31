from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import Item
from . forms import ItemForm
from django import *
# Create your views here.
@login_required
def item_list(response):
    item=Item.objects.all()
    return render(response,'item/item_list.html',{'item':item})

#@login_required
def item_add(response):
    form=ItemForm()
    if response.method == 'POST':
        form=ItemForm(response.POST or None)
        if form.is_valid():
            form.save()
            return redirect('item_list')
            message.success(response,'Item aded successfully')

    return render(response,'item/item_add.html',{'form':form})


def item_edit(response,pk):
    item=get_object_or_404(Item,pk=pk)
    form=ItemForm(response.POST or None,instance=item)
    if response.method == 'POST':
            form=ItemForm(response.POST or None,instance=item)
            if form.is_valid():
                 form.save()
            return redirect('item_list')
    else:
        form=ItemForm(instance=item)
        return render(response,'item/item_add.html',{'form':form})






def item_delete(response,pk):
    item=get_object_or_404(Item,pk=pk)
    if response.method == 'POST':
        item.delete()
        return redirect('item_list')
    
    return render(response,'item/item_delete.html',{'item':item})   