"""
URL configuration for EmpCRUD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp_form/',emp_form,name='emp_form'),
    path('emp_display/',emp_display,name='emp_display'),
    path('emp_update/<id>',emp_form,name='emp_update'),
    path('emp_delete/<id>',emp_delete,name='emp_delete'),
    path('filter_data/',filter_data,name='filter_data'),
    path('search/',search,name='search'),
    path('autocomplete/',autocomplete,name='autocomplete'),
]
