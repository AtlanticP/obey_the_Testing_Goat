from django.shortcuts import render, redirect
from .models import Item, List
from django.core.exceptions import ValidationError


def home_page(request):
	return render(request, 'home.html')

def list_view(request, list_id):
	
	lst = List.objects.get(pk=list_id)

	if request.method == 'POST':

		item = Item.objects.create(list=lst, text=request.POST['item_text'])

		return redirect(f'/list/{lst.id}/')

	return render(request, 'list.html', {'list': lst})

def new_list(request):

	lst = List.objects.create()
	item = Item(list=lst, text=request.POST['item_text'])	

	try:
		item.full_clean()
	except ValidationError as e:
		lst.delete()
		error = "You can't have an empty list item"
		return render(request, 'home.html', {'error': error})

	item.save()
	return redirect(f'/list/{lst.id}/')

def add_item(request, list_id):

	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect(f'/list/{list_id}/')
