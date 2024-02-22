from django.shortcuts import render
from .models import List

def get_index_page(request):
    lists = List.objects.all()
    return render(request, 'todos/index.html', {'lists': lists})

def get_product_details(request, pk):
    list = List.objects.get(id=pk)
    return render(request, 'todos/product-details.html', {'list': list})