#!/usr/bin/env python3
################################################
# The purpose of this function is to
# automatically complete my daily symptom
# survey
################################################

import webbrowser
from selenium import webdriver
import os

patient_connect_home="http://patientconnect.bu.edu/"
patient_connect_survey="https://patientconnect.bu.edu/Mvc/Patients/QuarantineSurvey"
patient_connect_mystery="https://patientconnect.bu.edu/CheckIn/Survey/ShowAll/21"

#kerbos_username=os.environ.get('KERBOS_USERNAME')
#kerbos_password=os.getenv('KERBOS_PASSWORD')

kerbos_username="e"
kerbos_password="2"

print(kerbos_username)
print(kerbos_password)

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

#webbrowser.open(patient_connect_home)
#chromedriver = os.popen("which chromedriver").read()
#print(chromedriver)
#driver = webdriver.Chrome(chromedriver)
#driver = webdriver.Chrome(executable_path=chromedrive_location)
#driver.get(patient_connect_home)



