from django.contrib import admin

from tarea_2_app.models import Concesion

class ConcesionAdmin(admin.ModelAdmin):
    list_display = ["id","tipo_de_concesion","comuna","lugar","n_rs_ds","tipo_tramite","concesionario","tipo_vigencia",]
    class meta:
        model = Concesion


admin.site.register(Concesion,ConcesionAdmin)
