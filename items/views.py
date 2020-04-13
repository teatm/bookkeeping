from django.shortcuts import render, get_object_or_404
from .models import Item, Category
# Create your views here.


def detail(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, 'items/detail.html', {"item": item})

def categories(request):
    categories = Category.objects.all()
    return render(request, 'items/categories.html', {"categories": categories})