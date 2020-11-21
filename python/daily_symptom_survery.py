#!/usr/bin/env python3
################################################
# The purpose of this function is to
# automatically complete my daily symptom
# survey
################################################
from selenium import webdriver
import time
import os

# links to be used later
patient_connect_home="http://patientconnect.bu.edu/"
patient_connect_survey="https://patientconnect.bu.edu/Mvc/Patients/QuarantineSurvey"

# set username and password
kerbos_username=os.getenv('KERBOS_USERNAME')
kerbos_password=os.getenv('KERBOS_PASSWORD')

# get to login page
driver = webdriver.Firefox()
driver.get(patient_connect_home)
time.sleep(1)

# fill in login & submit
user = driver.find_element_by_name("j_username")
user.send_keys(kerbos_username)
pasw = driver.find_element_by_name("j_password")
pasw.send_keys(kerbos_password)
driver.find_element_by_name("_eventId_proceed").click()

# go to form, fillin, submit
driver.get(patient_connect_survey)
driver.find_element_by_link_text("Continue").click()
#button_top = driver.find_element_by_class_name("col-xs-6"0).click()
buttons = driver.find_elements_by_class_name("answer.button.p-3")
i=1
for button in buttons:
    if (i % 2 ) != 0:
        button.click()
    i+=1
driver.find_element_by_class_name("btn.btn-lg.btn-success").click()
#print(button_top)
