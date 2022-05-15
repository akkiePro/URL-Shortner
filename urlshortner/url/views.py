from django.http import request
from django.shortcuts import render, redirect
from .models import url


# Create your views here.
def home(response):
    return render(response, "url/index.html")


def id(response, id):
    print(id)
    new_url = url.objects.get(id=id)
    print(new_url.main_link)
    return redirect(new_url.main_link)


def urlshortener(request):
    if request.method == 'POST':
        link_input = request.POST['link_input']
        URL = url(main_link=link_input)
        URL.save()

    new_url = url.objects.get(main_link=link_input)
    print(new_url.id)

    link= "http://127.0.0.1:8000/" + new_url.id
    return render(request, "url/index.html", {"link": link})
