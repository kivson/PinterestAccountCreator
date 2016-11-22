
import time
from selenium import webdriver

email = 'kivson+teste1234@gmail.com'
senha = 'teste@123'
nome_de_usuario = 'kivson_testes123'
idade_usuario = '27'


CHROME_DRIVER = "./bin/chromedriver"
browser = webdriver.Chrome(executable_path=CHROME_DRIVER)

browser.get('https://www.pinterest.com/')

input_mail = browser.find_element_by_name('id')
input_mail.send_keys('%s' % email)

input_pwd = browser.find_element_by_name('password')
input_pwd.send_keys('%s' % senha)

browser.find_element_by_css_selector('button[type="submit"]').click()

time.sleep(5)

nome_usuario = browser.find_element_by_name('full_name')
nome_usuario.send_keys(nome_de_usuario)

idade = browser.find_element_by_name('age')
idade.send_keys('%s' % idade_usuario)

browser.find_element_by_css_selector('button[type="submit"]').click()
