# 0 - ler o arquivo excel - ok
# 1 - lopar arquivo, loopar cada linha do arquivo excel - ok
#   1.1 - preencher os dados lidos para cada linha no navegador WEB - ok

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

file_name = "challenge.xlsx"
form_url = "https://rpachallenge.com/"

data = pd.read_excel(file_name)

chrome = webdriver.Chrome()
chrome.get(form_url)


for index, row in data.iterrows():
    label_first_name = chrome.find_element(
        By.CSS_SELECTOR, '[ng-reflect-name="labelFirstName"]'
    )
    label_last_name = chrome.find_element(
        By.CSS_SELECTOR, '[ng-reflect-name="labelLastName"]'
    )
    label_company_name = chrome.find_element(
        By.CSS_SELECTOR, '[ng-reflect-name="labelCompanyName"]'
    )
    label_role_in_company = chrome.find_element(
        By.CSS_SELECTOR, '[ng-reflect-name="labelRole"]'
    )
    label_address = chrome.find_element(
        By.CSS_SELECTOR, '[ng-reflect-name="labelAddress"]'
    )
    label_email = chrome.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelEmail"]')
    label_phone_number = chrome.find_element(
        By.CSS_SELECTOR, '[ng-reflect-name="labelPhone"]'
    )
    button = chrome.find_element(By.CLASS_NAME, "btn.uiColorButton")

    label_first_name.send_keys(row["First Name"])
    label_last_name.send_keys(row["Last Name "])
    label_company_name.send_keys(row["Company Name"])
    label_role_in_company.send_keys(row["Role in Company"])
    label_address.send_keys(row["Address"])
    label_email.send_keys(row["Email"])
    label_phone_number.send_keys(row["Phone Number"])

    button.click()

chrome.quit
