from django.db import models
import uuid
import os
# Create your models here.


class Area(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False, verbose_name="ID_Area")
    name = models.CharField(max_length=50, verbose_name="Nombre_Area")
    creation_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha_Area")

    def __str__(self) -> str:
        return self.name


class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False, verbose_name="ID_Departmento")
    name = models.CharField(max_length=55, verbose_name="Nombre_Departmento")
    description = models.TextField(verbose_name="Descripcion")
    area = models.ForeignKey(Area, verbose_name="Area_Departmento",
                             on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False, verbose_name="ID_Empleado")
    name = models.CharField(max_length=50, verbose_name="Nombre_Empleado")
    lastname = models.CharField(
        max_length=50, verbose_name="Apellido_Empleado")
    occupation = models.TextField(verbose_name="Ocupacion_Empleado")
    department = models.ForeignKey(
        Department, verbose_name="Departmento_Empleado", on_delete=models.CASCADE, null=True, blank=True)
    creation_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha_Empleado")
    avatar = models.ImageField(
        verbose_name="Avatar_Empleado", upload_to="employees")

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.avatar.path):
            os.remove(self.avatar.path)
        super(Employee, self).delete()

    def __str__(self) -> str:
        return self.name
