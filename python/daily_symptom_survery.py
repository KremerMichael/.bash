#!/usr/bin/env python3
################################################
# The purpose of this function is to
# automatically complete my daily symptom
# survey
################################################
# Imports
from selenium import webdriver
import argparse
import time
import os

################################################
# SET UP ARGUMENTS
################################################
parser = argparse.ArgumentParser(description='A function built to automatically complete the BU Daily Symptom Survey')
parser.add_argument('-u', '--username', help='kerbos username')
parser.add_argument('-p', '--password', help='kerbos password')
arguments = parser.parse_args()
# set username and password
if arguments.username is None:
    kerbos_username = os.getenv('KERBOS_USERNAME')
else:
    kerbos_username = arguments.username
if arguments.password is None:
    kerbos_password = os.getenv('KERBOS_PASSWORD')
else:
    kerbos_password = arguments.password

################################################
# LINKS 
################################################
PATIENT_CONNECT_HOME = "http://patientconnect.bu.edu/"
PATIENT_CONNECT_SURVEY = "https://patientconnect.bu.edu/Mvc/Patients/QuarantineSurvey"


################################################
# MAIN 
################################################
# Get login page
driver = webdriver.Firefox()
driver.get(PATIENT_CONNECT_HOME)
time.sleep(1)

# Login
user = driver.find_element_by_name("j_username")
user.send_keys(kerbos_username)
pasw = driver.find_element_by_name("j_password")
pasw.send_keys(kerbos_password)
driver.find_element_by_name("_eventId_proceed").click()

# Get form
driver.get(PATIENT_CONNECT_SURVEY)
driver.find_element_by_link_text("Continue").click()
# Fill out form
buttons = driver.find_elements_by_class_name("answer.button.p-3")
i=1
for button in buttons:
    if (i % 2 ) != 0:
        button.click()
    i+=1
#Submit form
driver.find_element_by_class_name("btn.btn-lg.btn-success").click()

# Get rid of geckodriver.log
print("WIP remove geckodriver.log")
################################################
# DONE
print('DONE')
################################################
