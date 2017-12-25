from django.db import models

class List(models.Model):
	pass

class Item(models.Model):
	text = models.TextField(default='')
	list_field = models.ForeignKey('List', on_delete=models.CASCADE)


