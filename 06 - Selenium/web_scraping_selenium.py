from selenium import webdriver
from time import sleep

navegador = webdriver.Chrome()

navegador.get('https://www.youtube.com/')

sleep(3)

elemento = navegador.find_element_by_tag_name('input')

elemento.send_keys('data')