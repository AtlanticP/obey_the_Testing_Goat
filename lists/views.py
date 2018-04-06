from django.shortcuts import render, redirect
from .models import Item, List
from django.core.exceptions import ValidationError
from lists.forms import ItemForm

form = ItemForm()

def home_page(request):
  return render(request, 'home.html', {'form': ItemForm()})

def new_list(request):

  if request.method == 'POST':
    form = ItemForm(data=request.POST)

    if form.is_valid():
      lst = List.objects.create()
      form.save(for_list=lst)
      return redirect(lst)
  return render(request, 'home.html', {'form': form})

def list_view(request, list_id):
  lst = List.objects.get(pk=list_id)
  form = ItemForm()
  # import pdb; pdb.set_trace()
  if request.method == 'POST':
    form = ItemForm(data=request.POST)
    if form.is_valid():
      form.save(for_list=lst)
      return redirect(lst)
  return render(request, 'list.html', {'list': lst, 'form': form})

