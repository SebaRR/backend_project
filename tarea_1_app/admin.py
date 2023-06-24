from django.contrib import admin

from tarea_1_app.models import Jurisprudencia, ValoresJurisprudencia

class InlineValores(admin.TabularInline):
    model = ValoresJurisprudencia
    extra = 0

class JurisprudenciaAdmin(admin.ModelAdmin):
    list_display = ["id","tipoCausa","rol","caratula","nombreProyecto","fechaSentencia","descriptores","activo","tribunal","visitas"]
    inlines = [InlineValores]
    class meta:
        model = Jurisprudencia


admin.site.register(Jurisprudencia,JurisprudenciaAdmin)