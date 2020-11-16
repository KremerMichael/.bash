import mechanize

br = mechanize.Browser()

patient_connect_login_url="http://patientconnect.bu.edu/"
patient_connect_survey_url="https://patientconnect.bu.edu/CheckIn/Survey/ShowAll/21"

br.open(patient_connect_login_url)
br.select_form(nr=0)

kerbos_username = "kremerme"
kerbos_password = "LErsbak85742"

print(br.form)
print()
print(br.form.controls)

for control in br.form.controls:
    print(control.name)
    if control.name == "j_username":
        print("writing {} {}".format(control.name, kerbos_username))
        br.form[control.name] = kerbos_username
        #control.value = kerbos_username
    elif control.name == "j_password":
        print("writing {} {}".format(control.name, kerbos_password))
        br.form[control.name] = kerbos_password
        #control.value = kerbos_password
    elif control.name == "_eventId_proceed":
        print() 
    #print(control.name)

login_response = br.submit()
login_response.close()
print(login_response)
print(login_response.read())
#print(login_response.form)

body = br.open(patient_connect_survey_url)
print(body.read())


#survey_respone = ?
