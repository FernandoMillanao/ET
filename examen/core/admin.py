from django.contrib import admin
from .models import Arbustos, Categoria, Flores, Registro, Tierradehojas, maceteros

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Flores)
admin.site.register(maceteros)
admin.site.register(Arbustos)
admin.site.register(Tierradehojas)
admin.site.register(Registro)
