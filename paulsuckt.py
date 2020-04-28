from selenium import webdriver

driver = webdriver.Chrome()

imt_user = "VincentHat"
imt_pw = "NenKleinenHehe"

driver.get("http://paul.uni-paderborn.de")
#Nutzernamefeld auswählen und Ausfüllen
username = driver.find_element_by_id("field_user")
username.clear()
username.send_keys(imt_user)
#Gleiches für Passwort
password = driver.find_element_by_id("field_pass")
password.clear()
password.send_keys(imt_pw)
#Login Button
driver.find_element_by_id("logIn_btn").click()

#Navigiere zu Studium > Semesterverwaltung
#Geht auch über id, aber wenig sprechend, deswegen über Title suchen
#Um das suchen über Title zu vereinfachen
title_search = lambda x: '//*[@title="{}"]'.format(x)
#Das war bissl nutzlos für zwei Aufrufe aber idc

driver.find_element_by_xpath(title_search("Studium")).click()
driver.find_element_by_xpath(title_search("Semesterverwaltung")).click()
#Navigiere über Veranstaltungsübersicht um sofort schneller zum konrekten Kurs zu kommen
driver.find_element_by_xpath(title_search("Veranstaltungs- übersicht")).click()
#Weil dynamische Generierung hier Suche über Linktext
driver.find_element_by_link_text('Datenstrukturen und Algorithmen - Übung 12').click()
driver.find_element_by_link_text('Material').click()

