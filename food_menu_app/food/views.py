from django.shortcuts import render, redirect

# Create your views here.

from .models import *
from django.http import HttpResponse
from .forms import *

def index(request):
    item_list = Item.objects.all()
    context = {'item_list': item_list,}
    return render(request, 'food/index.html', context)

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {'item': item,}
    
    return render(request, 'food/detail.html', context)


def create_item(request):
    form = ItemForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('food:index')
        
    context = {'form': form}
    return render(request, 'food/item-form.html', context)