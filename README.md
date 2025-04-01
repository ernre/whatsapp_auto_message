# 📩 WhatsApp Auto-Messenger (Python + Selenium)

This Python script automates sending messages to all **saved contacts** in your WhatsApp DM list using **Selenium and WhatsApp Web**.  
It **excludes** groups and unsaved numbers and ensures that each contact is only messaged **once**.

## ✨ Features
✅ Sends a message to all **saved contacts** in your DM list  
✅ **Excludes** groups and unsaved numbers  
✅ Ensures messages are **not sent twice** using a local file (`sent_contacts.txt`)  
✅ Automates **WhatsApp Web** login via QR code  

## 📌 Requirements
- **Python 3.x** installed
- **Google Chrome** (latest version)
- **ChromeDriver** (must be in system `PATH`)  
- **Selenium** (`pip install selenium`)
