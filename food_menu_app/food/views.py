from django.shortcuts import render, redirect, reverse
# Create your views here.

from .models import *
from django.http import HttpResponse
from .forms import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView

class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'

class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'
    context_object_name = 'item'

class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)
    
# def create_item(request):
#     form = ItemForm(request.POST or None)
    
#     if form.is_valid():
#         form.save()
#         return redirect('food:index')
        
#     context = {'form': form}
#     return render(request, 'food/item-form.html', context)

class UpdateItem(UpdateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item-form.html'

# class DeleteItem(DeleteView):
#     model = Item
#     template_name = 'food/item-delete.html'
#     success_url = reverse('food:index')

def delete_item(request, id):
    item = Item.objects.get(pk=id)
    
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    context = {'item': item}
    return render(request, 'food/item-delete.html', context)

# V1
# def index(request):
#     item_list = Item.objects.all()
#     context = {'item_list': item_list,}
#     return render(request, 'food/index.html', context)

# V1
# def detail(request, item_id):
#     item = Item.objects.get(pk=item_id)
#     context = {'item': item,}
    
#     return render(request, 'food/detail.html', context)

# V1
# def update_item(request, id):
#     item = Item.objects.get(pk=id)
#     form = ItemForm(request.POST or None, instance=item)
    
#     if form.is_valid():
#         form.save()
#         return redirect('food:index')
        
#     context = {'form': form, 'item': item}
#     return render(request, 'food/item-form.html', context)