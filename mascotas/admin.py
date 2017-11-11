from django.contrib import admin

from .models import Aviso, Estado, TiposDeEstados, Mascota

admin.site.register(Aviso)
admin.site.register(Estado)
admin.site.register(TiposDeEstados)
admin.site.register(Mascota)
