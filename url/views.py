from django.shortcuts import render,redirect
from .forms import surlform
from .models import SURL
from uuid import uuid4
# Create your views here.
def create(request):
    form = surlform()
    if request.method == 'POST':
        form = surlform(request.POST)
        if form.is_valid():
            link = form.cleaned_data['link']
            uuid = str(uuid4())[:7]
            short_url = f'bitly.fu/{uuid}'
            instance = SURL(link=link, uuid=uuid,urldic=short_url)
            instance.save()
    all_urls = SURL.objects.all()
    context = {'all_urls':all_urls,
                'form':form
                }
    return render(request, 'index.html', context)