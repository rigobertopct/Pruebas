from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Deporte)
admin.site.register(Disciplina)
admin.site.register(Departamento)
admin.site.register(Area)
admin.site.register(Servicios)
admin.site.register(Lugar)
admin.site.register(Evaluacion)
