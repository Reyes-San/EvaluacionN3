from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from core.models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
# Create your views here.


def home(request):
    return render(request, 'core/home.html')


class AreaListView(ListView):
    model = Area


class EmployeeListView(ListView):
    model = Employee


class DepartmentListView(ListView):
    model = Department


@method_decorator(staff_member_required, name='dispatch')
class AreaCreate(CreateView):
    model = Area
    form_class = AreaForm
    success_url = reverse_lazy('area_list')


@method_decorator(staff_member_required, name='dispatch')
class DepartmentCreate(CreateView):
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy('department_list')


@method_decorator(staff_member_required, name='dispatch')
class EmployeeCreate(CreateView):
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy('employee_list')


@method_decorator(staff_member_required, name='dispatch')
class AreaDelete(DeleteView):
    model = Area
    success_url = reverse_lazy('area_list')


@method_decorator(staff_member_required, name='dispatch')
class DepartmentDelete(DeleteView):
    model = Department
    success_url = reverse_lazy('department_list')

@method_decorator(staff_member_required, name='dispatch')
class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('employee_list')

@method_decorator(staff_member_required, name='dispatch')
class AreaUpdate(UpdateView):
    model = Area
    form_class = AreaForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('area_list')


@method_decorator(staff_member_required, name='dispatch')
class DepartmentUpdate(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('department_list')


@method_decorator(staff_member_required, name='dispatch')
class EmployeeUpdate(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('employee_list')


class AreaDetail(DetailView):
    model = Area


class DepartmentDetail(DetailView):
    model = Department


class EmployeeDetail(DetailView):
    model = Employee
