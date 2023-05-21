from django import forms
from app.models import *

gender=[
	('Male','Male'),
	('Female','Female')
]

class EmpForm(forms.ModelForm):
	class Meta:
		model=Employee
		fields='__all__'
		widgets={
			'empid':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Employee Id'}),
			'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Employee Name'}),
			'age':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Employee Age'}),
			'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Employee Email'}),
			'mobile':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Employee Mobile'}),
			'gender':forms.RadioSelect(choices=gender),
			'city':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Employee City'}),
			'position':forms.Select(attrs={'class':'form-control'})
		}

	def __init__(self,*args,**kwargs):
		super(EmpForm,self).__init__(*args,**kwargs)
		self.fields['position'].empty_label='---Select Employee Position---'

class FilterForm(forms.ModelForm):
	class Meta:
		model=Employee
		fields=['position']
		widgets={'position':forms.Select(attrs={'class':'form-control'})}
