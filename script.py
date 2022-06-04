import pandas as pd
from selenium import webdriver  # Permite navegar pelo browser.
import time
import urllib  # Biblioteca p/ codificação string --> url enconded

contact_list = pd.read_csv('./contacts_list.csv')
i_messages = enumerate(contact_list['Mensagem'])
# (0, msg_0), (1, msg_1), (2, msg_2)

browser = webdriver.Chrome()
browser.get('https://web.whatsapp.com/')

"""
Código que espera o carregamento da página exibida após o scan do QR Code
- 'side' é o elemento HTML que não existe na página de scan, mas existe na
página das conversas.
"""
while len(browser.find_elements_by_id('side')) < 1:
    time.sleep(1)

"""
Código que envia as mensagens para os respectivos contatos.
"""
for i, message in i_messages:
    contact_name = contact_list['Nome do Contato'][i]
    cellphone_num = contact_list['Número'][i]
    final_message = f'Olá {contact_name},\n{message}'
    encoded_message = urllib.parse.quote(final_message)
    link_wpp = f'https://web.whatsapp.com/send?phone={cellphone_num}&text={encoded_message}'

    print(f'Enviando mensagem p/ {contact_name}')
    browser.get(link_wpp)
    while len(browser.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')) < 1:
        time.sleep(1)

    send_btn = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
    send_btn.click()
    time.sleep(10)