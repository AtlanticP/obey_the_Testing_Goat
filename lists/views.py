from django.shortcuts import render, redirect
from .models import Item, List


def home_page(request):
	return render(request, 'home.html')

def list_view(request, list_id):
	lst = List.objects.get(pk=list_id)
	items = Item.objects.filter(list=lst)

	return render(request, 'list.html', {'items': items})

def new_list(request):

    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)

    return redirect('/list/{}/'.format(list_.id))  #!!! Trailing slash

def add_item(request, list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect(f'/list/{list_id}/')
