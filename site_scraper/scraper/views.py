from django.shortcuts import render

# Create your views here.
import requests
from bs4 import BeautifulSoup
from .models import *
from django.http import HttpResponseRedirect

def scrape(request):
    if request.method == 'POST':
        site = request.POST.get('site','')
        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')
                
        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            Link.objects.create(address=link_address, name=link_text)
        
        return HttpResponseRedirect('/')
    
    else:
        data = Link.objects.all()
            
    return render(request, 'scraper/result.html', {'data': data,})
          
def clear(request):
    Link.objects.all().delete()
    return render(request, 'scraper/result.html')