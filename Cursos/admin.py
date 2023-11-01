from django.contrib import admin
from .models import Curso, Alumno, instructor

admin.site.register(Curso)
admin.site.register(Alumno)
admin.site.register(instructor)

# Register your models here.
