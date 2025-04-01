import time
import re
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#önceden mesaj attığımız kişilere tekrardan atmamak için bu isimleri bir dosyaya alıyoruz
SENT_CONTACTS_FILE = "sent_contacts.txt"

def load_sent_contacts():
    if os.path.exists(SENT_CONTACTS_FILE):
        with open(SENT_CONTACTS_FILE, "r") as file:
            return set(file.read().splitlines())
    return set()

def save_sent_contact(contact):
    with open(SENT_CONTACTS_FILE, "a") as file:
        file.write(contact + "\n")

def is_saved_contact(chat_title):
    if re.fullmatch(r'\+?\d+', chat_title.strip()):  #kaydedilmemiş numaralardan kaçınmak için gerekli olan satır
        return False
    if ',' or '.' or 'BİLGİSAYAR FİZİK I' or 'Yerel Gençlik Koordinasyon Ağı' or 'Kaynak Paylaşım' or 'Notlar' or '2024/2025 Bahar İnternet Programcılığı'or 'Toplumsal Duyarlılık Projeleri' or 'IEEE İnönü | Kariyerine Yön Ver 🌏🚀💙' or 'Etkinlikler' or 'etkinlikler' or 'Ders' in chat_title:  #Gruplardan kaçınmak için yazılan kod, manuel olarak grup isimlerini yazmak gerekebilir
        return False
    return True

def send_message_to_chats(message):
    sent_contacts = load_sent_contacts()

    driver = webdriver.Chrome()
    driver.get('https://web.whatsapp.com')
    print("Please scan the QR code to log in to WhatsApp Web.")
    
    time.sleep(60)  

    chat_list_xpath = '//div[@id="pane-side"]//div[contains(@class, "chat")]'
    chats = driver.find_elements(By.XPATH, chat_list_xpath)
    
    print(f"Found {len(chats)} chats. Processing...")

    for chat in chats:
        try:
            title_elem = chat.find_element(By.XPATH, './/span[@dir="auto"]')
            chat_title = title_elem.text.strip()

            if is_saved_contact(chat_title) and chat_title not in sent_contacts:
                print(f"Sending message to: {chat_title}")
                chat.click()
                time.sleep(1)

                input_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
                input_box.send_keys(message)
                input_box.send_keys(Keys.ENTER)
                time.sleep(1)

                save_sent_contact(chat_title)  
            else:
                print(f"Skipping chat: {chat_title} (Already messaged or not a saved contact)")
        except Exception as e:
            print(f"Error processing chat: {e}")

    print("Done sending messages.")
    driver.quit()

if __name__ == '__main__':
    user_message = input("Enter the message to send: ")
    send_message_to_chats(user_message)
