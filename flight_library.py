import time
import contextlib
import json
from selenium import webdriver
import selenium.webdriver.support.ui as ui

def get_flights():
    with contextlib.closing(webdriver.PhantomJS()) as driver:
        while True:
            try:
                # initialize browser
                driver.get('http://newdau.angkasapura2.co.id/cp-mobile/flight/form')
                wait = ui.WebDriverWait(driver,25)

                # fill username
                driver.find_element_by_xpath("//input[@name='username']").send_keys('uapidummy')

                # fill password
                driver.find_element_by_xpath("//input[@name='password']").send_keys('Ymm4ipa')

                # Select airport
                driver.find_element_by_xpath("//select[@name='cabang']/option[text()='CGK - Soekarno-Hatta']").click()

                # Select API type
                driver.find_element_by_xpath("//select[@name='api']/option[text()='FIDS']").click()

                # submit
                driver.find_element_by_xpath("//input[@name='submit']").click()

                # wait until text body shows up
                wait.until(lambda driver: driver.find_element_by_xpath("//body"))

                # process json element
                flights = json.loads(driver.find_element_by_xpath("//body").text)

                # sleep
                time.sleep(1)

            except ValueError:
                continue
            break

        # return
        return flights
