from django.shortcuts import render, redirect
from .models import Item
from django.http import HttpResponse

def home_page(request):
	if request.method == 'POST':
		new_item_text = request.POST['item_text']
		Item.objects.create(text=new_item_text)
		return redirect('/lists/the-only-list-in-the-world/')				
		

	return render(request, 'home.html')

def list_view(request):
	items = Item.objects.all()

	return render(request, 'list.html', {'items': items})

def asd(request):
	pass