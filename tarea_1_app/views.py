import requests
import json

from django.shortcuts import redirect, render
from datetime import date
from tarea_1_app.forms import JurisprudenciaForm, ValoresJurisprudenciaForm
from tarea_1_app.models import Jurisprudencia, ValoresJurisprudencia

def date_formated(unformatted_date):
    date_list = unformatted_date.split("-")
    return date(int(date_list[2]), int(date_list[1]), int(date_list[0]))

def get_response():

    payload = {
        'orden': "nuevo",
        'page':1,
        'pageSize':20,
    }
    payload = json.dumps(payload)
    headers = {'content-type': 'application/json'}
    url = 'https://www.buscadorambiental.cl/buscador-api/jurisprudencias/list'
    response = requests.post(url,headers =headers, data=payload)
    response = response.text

    return response

def save_values(jurisprudence, values):

    for value in values:
        value = ValoresJurisprudenciaForm(value)
        is_form_valid = value.is_valid()
        if is_form_valid:
            value = value.save(commit=False)
            value.jurisprudencia = jurisprudence
            value.save()
        else:
            print(value.errors)


def save_jurisprudence(data):

    for item in data:
        values_list = item['valores']
        del item['valores']
        item["fechaSentencia"] = date_formated(item["fechaSentencia"])
        jurisprudence = JurisprudenciaForm(item)
        is_form_valid = jurisprudence.is_valid()
        if is_form_valid:
            jurisprudence = jurisprudence.save()
            save_values(jurisprudence, values_list)
        else:
            print(jurisprudence.errors)
        
def add_info_values(id_jurisprudence):
    values_list =[]
    values = ValoresJurisprudencia.objects.filter(jurisprudencia=id_jurisprudence)
    for value in values:
        value = value.__dict__
        values_list.append(value)
    return values_list


def add_info_jurisprudences(jurisprudences):
    jurisprudences_list = []
    for jurisprudence in jurisprudences:
        jurisprudence = jurisprudence.__dict__
        jurisprudence['values_data'] = add_info_values(jurisprudence['id'])
        jurisprudences_list.append(jurisprudence)
    return jurisprudences_list

def index(request):
    context = {}
    return render(request, 'index.html', context)

def tarea_1(request):
    context = {}

    response = get_response()
    response_loaded = json.loads(response)
    jurisprudence = response_loaded['jurisprudencias']
    save_jurisprudence(jurisprudence)
    jurisprudences = Jurisprudencia.objects.all()
    jurisprudences = add_info_jurisprudences(jurisprudences)
    context['response'] = jurisprudences
    
    return render(request, 'index_view_t1.html', context)


