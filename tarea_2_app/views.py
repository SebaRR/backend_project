from django.shortcuts import render
import json
# Create your views here.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def data_to_json():
    # data copiada a mano, para mostrar la creacion del archivo .json
    data = {}
    data['concesiones'] = []
    data['concesiones'].append({
        'n_concesion': '271',
        'tipo_concesion': 'Destinaciones',
        'comuna': 'TOCOPILLA',
        'lugar': 'PUERTO DE TOCOPILLA, COMUNA DE TOCOPILLA',
        'n_rs_ds':'744 DS',
        'tipo_tramite':'Otorgamiento',
        'concesionario':'---',
        'tipo_vigencia':'Entrada',
        })

    data['concesiones'].append({
        'n_concesion': '363',
        'tipo_concesion': 'Destinaciones',
        'comuna': 'TALTAL',
        'lugar': 'CALETA TALTAL, COMUNA DE TALTAL',
        'n_rs_ds':'121 DS',
        'tipo_tramite':'Otorgamiento',
        'concesionario':'MINISTERIO DE OBRAS PUBLICAS',
        'tipo_vigencia':'Entregada, con trámite en proceso',
        })
    
    data['concesiones'].append({
        'n_concesion': '420',
        'tipo_concesion': 'CCMM (1 a 10 años)',
        'comuna': 'MEJILLONES',
        'lugar': 'PUERTO DE MEJILLONES, COMUNA DE MEJILLONES',
        'n_rs_ds':'190 DS',
        'tipo_tramite':'Transferencia Total',
        'concesionario':'CORPESCA S.A.',
        'tipo_vigencia':'Entregada',
        })
    
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)



def tarea_2_script():
    driver = webdriver.Chrome()
    url = 'https://www.concesionesmaritimas.cl'
    driver.get(url)

    # Cambiar el contexto
    frameset1 = driver.find_element(By.TAG_NAME, 'frameset')
    driver.switch_to.frame(frameset1)

    frameset2 = driver.find_element(By.TAG_NAME, 'frameset')
    driver.switch_to.frame(frameset2)

    frame1 = driver.find_element(By.TAG_NAME, 'frame')
    driver.switch_to.frame(frame1)

    # Esperar hasta que el elemento <select> esté presente en el frame
    elemento_select1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'variableRegion')))
    elemento_select1.select_by_visible_text('II')
    elemento_select2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'variableGobmar')))
    elemento_select2.select_by_visible_text('GOBERNACIÓN MARÍTIMA ANTOFAGASTA')
    elemento_select3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'variableCapuerto')))
    elemento_select3.select_by_visible_text('ANTOFAGASTA')

    boton_filtrar = driver.find_element(By.NAME, 'verlistado')
    boton_filtrar.click()
    
    # Se obtienen los datos de la tabla
    wait = WebDriverWait(driver, 10)
    tabla = wait.find_element_by_css_selector('table[style*="color: #000080"]')

    filas = tabla.find_elements(By.TAG_NAME, 'tr')
    for fila in filas:
        celdas = fila.find_elements(By.TAG_NAME, 'td')
        for celda in celdas:
            print(celda.text)

    driver.quit()


