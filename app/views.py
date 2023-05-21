from django.shortcuts import render,redirect
from app.forms import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse

# Create your views here.

def emp_form(request,id=0):
	if id==0:
		form=EmpForm()
		if request.method=='POST':
			data=EmpForm(request.POST)
			if data.is_valid():
				name=data.cleaned_data['name']
				data.save()
				messages.success(request,f'{name} Data inserted successfully')
				return redirect('emp_display')
	else:
		ins=Employee.objects.get(empid=id)
		form=EmpForm(instance=ins)
		if request.method=='POST':
			data=EmpForm(request.POST,instance=ins)
			if data.is_valid():
				name=data.cleaned_data['name']
				data.save()
				messages.success(request,f'{name} Data updated successfully')
				return redirect('emp_display')

	return render(request,'employee_form.html',locals())

def emp_display(request):
	data=Employee.objects.all().order_by('empid')
	paginator=Paginator(data,5)
	page=request.GET.get('page')
	pages=paginator.get_page(page)
	form=FilterForm()
	return render(request,'emp_display.html',locals())


def emp_delete(request,id):
	data=Employee.objects.get(empid=id)
	data.delete()
	messages.success(request,f'{data.name} Details deleted successfully')
	return redirect('emp_display')

def filter_data(request):
	if request.method=='GET':
		data=FilterForm(request.GET)
		if data.is_valid():
			id=data.cleaned_data['position']
			fil=Employee.objects.filter(position=id)
	return render(request,'filter_data.html',locals())

def search(request):
	search=request.GET['search']
	if not search=='':
		data=Employee.objects.filter(name__icontains=search)
	return render(request,'search.html',locals())

def autocomplete(request):
	if 'term' in request.GET:
		qs=Employee.objects.filter(name__istartswith=request.GET['term'])
		titles=[]
		for item in qs:
			titles.append(item.name)
		return JsonResponse(titles,safe=False)