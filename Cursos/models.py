from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    diasDeLaSemana = models.CharField(max_length=100)
    FechaInicio = models.DateField()
    FechaFinal = models.DateField()
    instructor = models.ForeignKey('instructor' , on_delete=models.CASCADE, blank=True, null=True) 
    alumnos = models.ManyToManyField('Alumno' , blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    Documento= models.IntegerField()
    domicilio = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    genero= models.CharField(max_length=100)
    # cursos = models.ManyToManyField('Cursos')


    def __str__(self):
        return f'{self.nombre}, {self.apellido}'

class instructor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    Documento= models.IntegerField()
    domicilio = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    genero= models.CharField(max_length=100)
    # cursos = models.ManyToManyField('Cursos')
    
    def __str__(self):
        return f'{self.nombre}, {self.apellido}'