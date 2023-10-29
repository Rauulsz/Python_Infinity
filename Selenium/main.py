#IMPORTANDO
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pyttsx3

opcoes = Options()
opcoes.add_experimental_option("detach", True)

#PUXANDO O SITE
navegador = webdriver.Chrome(options=opcoes)
navegador.maximize_window()
navegador.get("https://www.contosdeterror.site/")

leia_mais = navegador.find_element(By.XPATH, '//*[@id="Blog1"]/div[1]/article[6]/div/div/div[4]/div[2]/a')

leia_mais.click()

texto_final = ""

#PEDINDO TODOS OS PARAGRAFOS EM LOOP
for i in range(7, 32):
    paragrafo = navegador.find_element(By.XPATH, f'//*[@id="post-body-170950715524830154"]/p[{i}]/span')
    texto_final += paragrafo.text

#CRIANDO O NARRADOR
narrador = pyttsx3.init()
narrador.setProperty("rate", 150)
narrador.say(texto_final)
narrador.runAndWait

