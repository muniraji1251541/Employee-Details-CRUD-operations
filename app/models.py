from django.db import models
from django import forms
import re

# Create your models here.



def name_valid(value):
	if len(value)<=3:
		raise forms.ValidationError('Name length is short')


def age_valid(value):
	if value<=20:
		raise forms.ValidationError('Age must be more then 20')

def mobile_valid(value):
	pattern=re.compile('[6-9][0-9]{9}')
	if not pattern.match(value):
		raise forms.ValidationError('Invalid mobile number')

class Position(models.Model):
	name=models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Employee(models.Model):
	empid=models.IntegerField(primary_key=True)
	name=models.CharField(validators=[name_valid],max_length=100)
	age=models.IntegerField(validators=[age_valid])
	email=models.EmailField()
	mobile=models.CharField(validators=[mobile_valid],max_length=10)
	gender=models.CharField(max_length=6)
	city=models.CharField(max_length=100)
	position=models.ForeignKey(Position,on_delete=models.CASCADE)

	def __str__(self):
		return self.name

