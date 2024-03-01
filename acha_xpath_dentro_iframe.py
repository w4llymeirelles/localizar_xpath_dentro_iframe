#não esquecer de dar os imports
"""
import selenium
import webdriver...
"""


#MUDA PARA O IFRAME QUE CONTÉM O ELEMENTO
iframe = driver.find_element(By.ID, 'ssoFrame')
driver.switch_to.frame(iframe)


# Agora, você está dentro do iframe. Você pode localizar o elemento desejado dentro dele.
botao_certificado_digital = driver.find_element(By.XPATH, '//*[@id="kc-pje-office"]')

botao_certificado_digital.click()


time.sleep(3)
# Aguarde até que a página esteja completamente carregada
WebDriverWait(driver, 1).until(
    lambda driver: driver.execute_script('return document.readyState') == 'complete'
)

try:
    # Aguarde até que o elemento "botao-menu" seja visível
    elemento_botao_menu = WebDriverWait(driver, 1).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'botao-menu'))
    )

    # Interagir com o elemento
    elemento_botao_menu.click()

except TimeoutException:
    print("O elemento 'botao-menu' não foi encontrado dentro do tempo limite.")

finally:
    # Fechar o navegador
    print('encotrei elemento')
