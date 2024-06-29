from django.shortcuts import render

# Create your views here.
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
    else:
        form = PostCreateForm(data=request.GET, files=request.FILES)
        
    return render(request, 'posts/create.html', {'form': form})

