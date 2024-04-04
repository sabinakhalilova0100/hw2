from django.shortcuts import render, redirect, get_object_or_404
from .models import List
from .forms import CreateTodosForm, EditTodosForm
from django.contrib import messages

def index_page_view(request):
    return redirect('/lists')


def lists_page_view(request):
    if request.method == 'GET':
        form = CreateTodosForm()
        lists = List.objects.all()
        return render(request, 'todos/index.html', {'lists': lists, 'form': form})
    if request.method == 'POST':
        print(request.POST)
        # title = request.POST.get('title', '')
        # description = request.POST.get('description', '')
        # due_date = request.POST.get('due_date', '')
        # status = request.POST.get('status', '') == 'on'

        form = CreateTodosForm(request.POST)

        if form.is_valid():
            title = form.data.get('title')
            description = form.data.get('description')
            due_date = form.data.get('due_date')
            enabled = form.data.get('status')
            status = False
            if enabled == 'on':
                status = True
            list = List(title=title, description=description,due_date=due_date, status=status)
            list.save()
        lists = List.objects.all()
        return render(request, 'todos/index.html', {'lists': lists, 'form': form})




        # form = CreateTodosForm(request.POST)

        # if form.is_valid():
        #     title = form.data.get('title')
        #     description = form.data.get('description')
        #     due_date = form.data.get('due_date')
        #     status = form.data.get('status')
        #     list = List(title=title, description=description, due_date=due_date, status=status)
        #     list.save()
        # lists = List.objects.all()
        # return render(request, 'todos/index.html', {'lists': lists, 'form': form})


def product_details_view(request, pk):
    list = List.objects.get(id=pk)
    return render(request, 'todos/product-details.html', {'list': list})


def delete_list_page_view(request, pk):
    try:
        list = List.objects.get(id=pk)
        list.delete()
        return redirect('/lists')
    except List.DoesNotExist:
        error = 'List Does Not Found'
        messages.error(request, message=error)
        return redirect('/lists')
        # form = CreateTodosForm
        # lists = List.objects.all()
        # return render(request, 'todos/index.html', {'lists': lists, 'form': form, 'error': error })
        # # return redirect('/lists')

def edit_list_page_view(request, pk):
    list_item = get_object_or_404(List, pk=pk)
    if request.method == 'POST':
        form = EditTodosForm(request.POST, instance=list_item)
        if form.is_valid():
            form.save()
            messages.success(request, 'List updated successfully')
            return redirect(f'/lists/{pk}')
    else:
        form = EditTodosForm(instance=list_item)
    return render(request, 'todos/edit-product.html', {'form': form})


