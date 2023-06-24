from django import forms
from tarea_1_app.models import Jurisprudencia, ValoresJurisprudencia


class JurisprudenciaForm(forms.ModelForm):
    class Meta:
        model = Jurisprudencia
        fields = (
            'id','tipoCausa', 'rol', 'caratula', 'nombreProyecto', 'fechaSentencia', 'descriptores', 
            'linkSentencia', 'urlSentencia', 'activo', 'tribunal', 'tipo', 'relacionada', 'visitas',
            )
        
class ValoresJurisprudenciaForm(forms.ModelForm):
    class Meta:
        model = ValoresJurisprudencia
        fields = (
            'id','idParametro','idItemlista','valor','parametro','item','jurisprudencia',
        )