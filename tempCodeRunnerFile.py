for i, message in i_messages:
#     contact_name = contact_list["Nome do Contato"][i]
#     cellphone_num = contact_list["Número"][i]
#     final_message = f"Olá {contact_name},\n{message}"
#     encoded_message = urllib.parse.quote(final_message)
#     link = f"https://web.whatsapp.com/send?phone={cellphone_num}&text={encoded_message}"

#     browser.get(link)
#     while len(browser.find_elements_by_id("side")) < 1:
#         time.sleep(1)