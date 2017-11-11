from django.contrib import admin

from .models import Evento


class EventoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'tipo',
        'titulo',
        #'autor',
        'fecha_creacion'
    ]
    raw_id_fields = ['autor']


admin.site.register(Evento, EventoAdmin)
