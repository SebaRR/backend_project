from django.shortcuts import render

# Create your views here.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def tarea_2_script():
    driver = webdriver.Chrome()
    url = 'https://www.concesionesmaritimas.cl'
    driver.get(url)

    #filtrar 
    #filtro1 = driver.find_element(By.NAME, 'variableRegion')
    #filtro1.select_by_visible_text('2')
    """#filtro1.send_keys('2')
    filtro2 = driver.find_element(By.NAME, 'variableGobmar')
    filtro2.send_keys('GOBERNACIÓN MARÍTIMA ANTOFAGASTA')
    filtro3 = driver.find_element(By.NAME, 'variableCapuerto')
    filtro3.send_keys('ANTOFAGASTA')
    boton_filtrar = driver.find_element(By.NAME, 'verlistado')
    boton_filtrar.click()

    wait = WebDriverWait(driver, 10)
    tabla = wait.find_element_by_css_selector('table[style*="color: #000080"]')

    filas = tabla.find_elements(By.TAG_NAME, 'tr')
    for fila in filas:
        celdas = fila.find_elements(By.TAG_NAME, 'td')
        for celda in celdas:
            print(celda.text)"""

    #elemento_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'variableRegion')))

    # Acciones adicionales con el elemento select
    # Por ejemplo, obtener las opciones seleccionables:

    # Cambiar al contexto del primer frame
    frameset1 = driver.find_element(By.TAG_NAME, 'frameset')
    driver.switch_to.frame(frameset1)

    frame1 = driver.find_element(By.TAG_NAME, 'frame')
    driver.switch_to.frame(frame1)

    # Cambiar al contexto del segundo frameset
    frameset2 = driver.find_element(By.TAG_NAME, 'frameset')
    driver.switch_to.frame(frameset2)

    # Cambiar al contexto del segundo frame
    frame2 = driver.find_element(By.TAG_NAME, 'frame')
    driver.switch_to.frame(frame2)

    # Esperar hasta que el elemento <select> esté presente en el frame
    elemento_select = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'variableRegion'))
    )

    # Acciones adicionales con el elemento <select>
    opciones = elemento_select.find_elements(By.TAG_NAME, 'option')
    for opcion in opciones:
        print(opcion.text)

    # Cambiar de nuevo al contexto predeterminado
    

    driver.quit()

tarea_2_script()
