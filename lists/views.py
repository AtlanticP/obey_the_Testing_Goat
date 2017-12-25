from django.shortcuts import render, redirect
from .models import Item, List

def home_page(request):
	
	return render(request, 'home.html')

def list_view(request):
	items = Item.objects.all()

	return render(request, 'list.html', {'items': items})

def new_list(request):
    list_field = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list_field=list_field)

    return redirect('/lists/the-only-list-in-the-world/')
