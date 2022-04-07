from wsgiref import headers

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_argument('--headless') #não mostrar o navegador
options.add_argument('window-size=400,800')
options.add_experimental_option("detach", True)

s = Service('C:/Users/marco/Downloads/chromedriver.exe')
navegador = webdriver.Chrome(service=s, options=options)
navegador.get('https://marcosruizmrf.github.io/front-pgf/')
sleep(2)

button_stay = navegador.find_element_by_css_selector('button > span')
#como clicar no segundo botao do site?
#nextButton = navegador.find_elements_by_tag_name('button')[-4]
button_stay.click()

sleep(4)

page_content = navegador.page_source
site = BeautifulSoup(page_content, 'html.parser')
print(site.prettify())
sleep(2)
noticia = site.findAll("mat-card-header")
for header in noticia:
   header.get('class'), print(header.find('mat-card-title').text[0:20])

'''
input_place = navegador.find_element_by_tag_name('input')
input_place.send_keys('São Paulo')
input_place.submit()
'''



