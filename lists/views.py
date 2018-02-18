from django.shortcuts import render, redirect
from .models import Item, List
from django.core.exceptions import ValidationError
# from superlists.settings import BASE_DIR, STATICFILES_DIR



def home_page(request):
	return render(request, 'home.html')

def list_view(request, list_id):
	lst = List.objects.get(pk=list_id)

	return render(request, 'list.html', {'list': lst})

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

def add_item(request, list_id):

	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect(f'/list/{list_id}/')
