"""evaluacionN3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from core import views
from core.views import *
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # rutas para el modulo area
    path('area_list/', AreaListView.as_view(), name='area_list'),
    path('area_register/', AreaCreate.as_view(), name='area_register'),
    path('area_deleted/<str:pk>/',
         AreaDelete.as_view(), name='area_deleted'),
    path('area_edit/<str:pk>/', AreaUpdate.as_view(), name='area_edit'),
    path('area_detail/<str:pk>/',
         AreaDetail.as_view(), name='area_detail'),
    # rutas para el modulo departments
    path('department_list/', DepartmentListView.as_view(), name='department_list'),
    path('department_register/', DepartmentCreate.as_view(),
         name='department_register'),
    path('department_deleted/<str:pk>/',
         DepartmentDelete.as_view(), name='department_deleted'),
    path('department_edit/<str:pk>/',
         DepartmentUpdate.as_view(), name='department_edit'),
    path('department_detail/<str:pk>/',
         DepartmentDetail.as_view(), name='department_detail'),

    # rutas para el modulo employees
    path('employee_list/', EmployeeListView.as_view(), name='employee_list'),
    path('employee_register/', EmployeeCreate.as_view(), name='employee_register'),
    path('employee_deleted/<str:pk>/',
         EmployeeDelete.as_view(), name='employee_deleted'),
    path('employee_edit/<str:pk>/', EmployeeUpdate.as_view(), name='employee_edit'),
    path('employee_detail/<str:pk>/',
         EmployeeDetail.as_view(), name='employee_detail'),

    # rutas para los perfiles que podran mirar dichos modulos
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
