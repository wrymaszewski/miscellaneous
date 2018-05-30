import os
from bs4 import BeautifulSoup
import datetime
from time import sleepimport datetime
from selenium import webdriver

email = input("Enter email: ")
password = input('Enter password: ')
month = input('Enter month: ')
day = input("Enter day: ")
interval = input('Enter time interval: ')
clicks = int(month) - datetime.date.today().month
br = False
url1 = "http://kolejka-wsc.mazowieckie.pl/rezerwacje/pol/login"
url2 = "http://kolejka-wsc.mazowieckie.pl/rezerwacje/pol/queues/200064/200084"

while True:
    driver = webdriver.Chrome()
    driver.get(url1)
    driver.find_element_by_id("UserEmail").send_keys(email)
    driver.find_element_by_id("UserPassword").send_keys(password)
    driver.find_element_by_xpath("//input[@value='Zaloguj']").click()
    driver.get(url2)
    driver.execute_script('document.getElementById("terms").click()')
    driver.find_element_by_tag_name("button").click()

    # changing calendar to chosen month
    for i in range(clicks):
        driver.find_element_by_class_name("fa-chevron-circle-right").click()
    source = driver.page_source
    soup = BeautifulSoup(source, 'lxml')

    # choose active days
    divs = soup.find_all("div", class_="day good")

    # ring an alarm if chosen day is active
    for div in divs:
        if str(day) == str(div.text):
            print(str(datetime.datetime.now()) + " ---> " + "CHOSEN DAY ACTIVE :)")
            os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (10, 440))
            br = True
    driver.close()
    if br:
        break
    else:
        print(str(datetime.datetime.now()) + " ---> " + "chosen day not active :(")
    sleep(int(interval))
