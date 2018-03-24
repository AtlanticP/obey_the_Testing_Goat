from django.shortcuts import render, redirect
from .models import Item, List
from django.core.exceptions import ValidationError


def home_page(request):
	return render(request, 'home.html')

def new_list(request):

	lst = List.objects.create()
	item = Item(list=lst, text=request.POST['item_text'])	

	try:
		item.full_clean()
	except ValidationError:
		lst.delete()
		error = "You can't have an empty list item"
		return render(request, 'home.html', {'error': error})

	item.save()
	return redirect(lst)

def list_view(request, list_id):
	
	lst = List.objects.get(pk=list_id)

	if request.method == 'POST':

		item = Item.objects.create(list=lst, text=request.POST['item_text'])

		try:
			item.full_clean()
		except ValidationError:
			error = "You can't have an empty list item"
			return render(request, 'list.html', {'list': lst, 'error': error})

		item.save()	
		return redirect(lst)

	return render(request, 'list.html', {'list': lst})

def add_item(request, list_id):

	lst = List.objects.get(id=list_id)

	item = Item.objects.create(text=request.POST['item_text'], list=lst)
	
	try:
		item.full_clean()
	except ValidationError:
		error = "You can't have an empty list item"
		return render(request, 'list.html', {'list':lst, 'error':error})
	item.save()
	return redirect(lst)
