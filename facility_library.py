import time
import contextlib
import json
from selenium import webdriver
import selenium.webdriver.support.ui as ui

def get_restaurants():
    with contextlib.closing(webdriver.PhantomJS()) as driver:
        while True:
            try:
                # initialize browser
                driver.get('http://newdau.angkasapura2.co.id/cp-mobile/facility/form')
                wait = ui.WebDriverWait(driver,25)

                # fill username
                driver.find_element_by_xpath("//input[@name='username']").send_keys('uapidummy')

                # fill password
                driver.find_element_by_xpath("//input[@name='password']").send_keys('Ymm4ipa')

                # Select airport
                driver.find_element_by_xpath("//select[@name='cabang']/option[text()='CGK - Soekarno-Hatta']").click()

                # Select facility as Diner
                driver.find_element_by_xpath("//select[@name='data_type']/option[text()='DINE']").click()

                # submit
                driver.find_element_by_xpath("//input[@name='submit']").click()

                # wait until text body shows up
                wait.until(lambda driver: driver.find_element_by_xpath("//body"))

                # process json element
                restaurants = json.loads(driver.find_element_by_xpath("//body").text)

                # sleep
                time.sleep(1)

            except ValueError:
                continue
            break

        # return
        return restaurants

def get_facilities():
    with contextlib.closing(webdriver.PhantomJS()) as driver:
        while True:
            try:
                # initialize browser
                driver.get('http://newdau.angkasapura2.co.id/cp-mobile/facility/form')
                wait = ui.WebDriverWait(driver,25)

                # fill username
                driver.find_element_by_xpath("//input[@name='username']").send_keys('uapidummy')

                # fill password
                driver.find_element_by_xpath("//input[@name='password']").send_keys('Ymm4ipa')

                # Select airport
                driver.find_element_by_xpath("//select[@name='cabang']/option[text()='CGK - Soekarno-Hatta']").click()

                # Select facility as Diner
                driver.find_element_by_xpath("//select[@name='data_type']/option[text()='FACILITIES']").click()

                # submit
                driver.find_element_by_xpath("//input[@name='submit']").click()

                # wait until text body shows up
                wait.until(lambda driver: driver.find_element_by_xpath("//body"))

                # process json element
                facilities = json.loads(driver.find_element_by_xpath("//body").text)

                # sleep
                time.sleep(1)

            except ValueError:
                continue
            break

        # return
        return facilities

def get_hotels():
    with contextlib.closing(webdriver.PhantomJS()) as driver:
        while True:
            try:
                # initialize browser
                driver.get('http://newdau.angkasapura2.co.id/cp-mobile/facility/form')
                wait = ui.WebDriverWait(driver,25)

                # fill username
                driver.find_element_by_xpath("//input[@name='username']").send_keys('uapidummy')

                # fill password
                driver.find_element_by_xpath("//input[@name='password']").send_keys('Ymm4ipa')

                # Select airport
                driver.find_element_by_xpath("//select[@name='cabang']/option[text()='CGK - Soekarno-Hatta']").click()

                # Select facility as Diner
                driver.find_element_by_xpath("//select[@name='data_type']/option[text()='HOTEL']").click()

                # submit
                driver.find_element_by_xpath("//input[@name='submit']").click()

                # wait until text body shows up
                wait.until(lambda driver: driver.find_element_by_xpath("//body"))

                # process json element
                hotels = json.loads(driver.find_element_by_xpath("//body").text)

                # sleep
                time.sleep(1)

            except ValueError:
                continue
            break

        # return
        return hotels

def get_important_numbers():
    with contextlib.closing(webdriver.PhantomJS()) as driver:
        while True:
            try:
                # initialize browser
                driver.get('http://newdau.angkasapura2.co.id/cp-mobile/facility/form')
                wait = ui.WebDriverWait(driver,25)

                # fill username
                driver.find_element_by_xpath("//input[@name='username']").send_keys('uapidummy')

                # fill password
                driver.find_element_by_xpath("//input[@name='password']").send_keys('Ymm4ipa')

                # Select airport
                driver.find_element_by_xpath("//select[@name='cabang']/option[text()='CGK - Soekarno-Hatta']").click()

                # Select facility as Diner
                driver.find_element_by_xpath("//select[@name='data_type']/option[text()='IMPORTANT NUMBER']").click()

                # submit
                driver.find_element_by_xpath("//input[@name='submit']").click()

                # wait until text body shows up
                wait.until(lambda driver: driver.find_element_by_xpath("//body"))

                # process json element
                important_numbers = json.loads(driver.find_element_by_xpath("//body").text)

                # sleep
                time.sleep(1)

            except ValueError:
                continue
            break

        # return
        return important_numbers

def get_shops():
    with contextlib.closing(webdriver.PhantomJS()) as driver:
        while True:
            try:
                # initialize browser
                driver.get('http://newdau.angkasapura2.co.id/cp-mobile/facility/form')
                wait = ui.WebDriverWait(driver,25)

                # fill username
                driver.find_element_by_xpath("//input[@name='username']").send_keys('uapidummy')

                # fill password
                driver.find_element_by_xpath("//input[@name='password']").send_keys('Ymm4ipa')

                # Select airport
                driver.find_element_by_xpath("//select[@name='cabang']/option[text()='CGK - Soekarno-Hatta']").click()

                # Select facility as Diner
                driver.find_element_by_xpath("//select[@name='data_type']/option[text()='SHOP']").click()

                # submit
                driver.find_element_by_xpath("//input[@name='submit']").click()

                # wait until text body shows up
                wait.until(lambda driver: driver.find_element_by_xpath("//body"))

                # process json element
                shops = json.loads(driver.find_element_by_xpath("//body").text)

                # sleep
                time.sleep(1)

            except ValueError:
                continue
            break

        # return
        return shops
