from django.shortcuts import render, redirect

# Create your views here.
from .models import *

def index(request):
    if request.method == 'POST':
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume_model = Consume(user=user, food_consumed=consume)
        consume_model.save()
        foods = Food.objects.all()
        
    
    else:
        foods = Food.objects.all()
        
    consumed_food = Consume.objects.filter(user=request.user)
    context = {'foods': foods, 'consumed_food': consumed_food}
    return render(request, 'tracker/index.html', context)


def reset(request):
    consumed_food = Consume.objects.filter(user=request.user)
    consumed_food.delete()
    return redirect('/')

def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/')
    
    return render(request, 'tracker/delete.html')