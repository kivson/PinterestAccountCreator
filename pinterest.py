import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

CHROME_DRIVER = "./bin/chromedriver"


browser = webdriver.Chrome(executable_path=CHROME_DRIVER)
browser.implicitly_wait(1)
waiter = WebDriverWait(browser, 20)


def criar_conta(usuario):

    _tenta_login(usuario)

    try:
        nome_usuario = waiter.until(EC.presence_of_element_located((By.NAME, 'full_name')))
    except NoSuchElementException:
        usuario['criado'] = False
        return usuario

    nome_usuario.send_keys(usuario['nome_de_usuario'])

    idade = browser.find_element_by_name('age')
    idade.send_keys('%s' % usuario['idade_usuario'])

    browser.find_element_by_css_selector('button[type="submit"]').click()

    try:
        time.sleep(5)
        browser.find_element_by_class_name('NuxAppUpsell').find_element_by_css_selector('button').click()
    except:
        pass

    try:
        waiter.until(EC.presence_of_element_located((By.CLASS_NAME, 'interestImage')))
        for i in browser.find_elements_by_class_name('interestImage')[:7]:
            i.click()
        browser.find_element_by_class_name('footer').find_element_by_css_selector('button').click()

        waiter.until(EC.presence_of_element_located((By.CLASS_NAME, 'optionalSkip'))).click()

        waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.confirm'))).click()

    except NoSuchElementException:
        pass

    waiter.until(EC.presence_of_element_located((By.CLASS_NAME, 'bannerText')))

    usuario['criado'] = True
    return usuario


def seguir_conta(urls_perfis, usuario):

    _tenta_login(usuario)
    waiter.until(EC.presence_of_element_located((By.CLASS_NAME, 'usernameLink')))

    for url in urls_perfis:
        browser.get(url=url)

        element = waiter.until(EC.element_to_be_clickable((By.XPATH, "//*[text() = 'Seguir']")))
        element.click()

        waiter.until(EC.element_to_be_clickable((By.XPATH, "//*[text() = 'Deixar de seguir']")))

    return usuario


def _tenta_login(usuario):
    browser.delete_all_cookies()
    browser.get('https://www.pinterest.com/')
    input_mail = browser.find_element_by_name('id')
    input_mail.send_keys('%s' % usuario['email'])
    input_pwd = browser.find_element_by_name('password')
    input_pwd.send_keys('%s' % usuario['senha'])
    browser.find_element_by_css_selector('button[type="submit"]').click()