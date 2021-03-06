from django.shortcuts import render, redirect
from .models import Item, List
from django.core.exceptions import ValidationError
from lists.forms import ItemForm



def home_page(request):
	return render(request, 'home.html', {'form': ItemForm()})

def list_view(request, list_id):
	
	lst = List.objects.get(pk=list_id)
	error = None
	
	if request.method == 'POST':
		try:
			item = Item(text = request.POST['item_text'], list=lst)
			item.full_clean()
			item.save()
			return redirect(f'/list/{lst.id}/')
		
		except ValidationError:
			error = "You can't have an empty list item"

	return render(request, 'list.html', {'list': lst, 'error': error} )

def new_list(request):
	list_ = List.objects.create()
	item = Item.objects.create(text=request.POST['item_text'], list=list_)
	try:
		item.full_clean()
	except ValidationError:
		list_.delete()
		error = "You can't have an empty list item"
		return render(request, 'home.html', {"error": error})
		# return redirect(f'/')
	return redirect(f'/list/{list_.id}/')  #!!! Trailing slash

