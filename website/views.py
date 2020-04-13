from django.shortcuts import render

from items.models import Item
# Create your views here.

def home(request):
    return render(request, "website/home.html", {"items": Item.objects.all()})