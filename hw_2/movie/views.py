from django.shortcuts import render
from .models import Films
# Create your views here.
def get_index_page(request):
    films = Films.objects.all()
    return render(request, 'movie/index.html', {'films': films})


def get_product_details(request, pk):
    film = Films.objects.get(id=pk)
    return render(request, 'movie/product-details.html', {'film': film})
