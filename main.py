from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import random
import inputDataGen

PATH = r"C:\Users\hlsmirn\PycharmProjects\OISelTest\WebDrivers\chromedriver.exe"
CV_PATH = r"C:\Users\hlsmirn\PycharmProjects\OISelTest\InputFiles\tmp.doc"

driver = webdriver.Chrome(PATH)
driver.get('https://www.orioninc.com')
actions = ActionChains(driver)


def accept_cookie_policy():
    if driver.find_element(By.ID, "hs-eu-cookie-confirmation"):
        driver.find_element(By.XPATH, "//*[@id='hs-eu-confirmation-button']").click()


def do_careers_navigation():
    menu = driver.find_element(By.CSS_SELECTOR, ".nav")
    company_submenu = driver.find_element(By.CSS_SELECTOR, "li.nav-item:nth-child(9)")
    company_careers_submenu = driver.find_element(By.CSS_SELECTOR, "a.nav-link:nth-child(6)")

    actions.move_to_element(menu)
    actions.move_to_element(company_submenu)
    actions.click(company_careers_submenu)
    actions.perform()


def do_regions_scroll():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    regions_block = driver.find_element(By.CSS_SELECTOR, ".wp-container-6")
    cord = regions_block.location.values()

    driver.execute_script(f"window.scroll({cord.mapping.get('x')}, {cord.mapping.get('y')});")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".wp-image-11476")))
    regions_block.find_element(By.CSS_SELECTOR, ".wp-image-11476").click()


def search_vacancy():
    search_field_xpath = "/html/body/main/div[2]/div/div/div[2]/div[1]/form/input[1]"
    search_field = driver.find_element(By.XPATH, search_field_xpath)
    search_field.click()
    actions.send_keys_to_element(search_field, "Robot+Python").send_keys(Keys.ENTER).perform()


def select_vacancy():
    try:
        nec_vacancy = driver.find_element(By.PARTIAL_LINK_TEXT, "Robot+Python")
    except NoSuchElementException:
        print("no 'Robot+Python' vacancy were found")
        return

    nec_vacancy.click()


def apply_now():
    in_data = inputDataGen.InputFieldGenerator()
    full_name = in_data.get_full_name()

    driver.find_element(By.PARTIAL_LINK_TEXT, "Apply Now").click()

    actions.send_keys_to_element(driver.find_element(By.ID, "input_7_2"), full_name[0])  # first name
    actions.send_keys_to_element(driver.find_element(By.ID, "input_7_3"), full_name[1])  # last name

    actions.send_keys_to_element(driver.find_element(By.ID, "input_7_4"), in_data.get_email())
    actions.send_keys_to_element(driver.find_element(By.ID, "input_7_5"), in_data.get_phone())
    actions.send_keys_to_element(driver.find_element(By.ID, "input_7_7"), in_data.get_state())
    actions.send_keys_to_element(driver.find_element(By.ID, "input_7_8"), in_data.get_city())
    actions.send_keys_to_element(driver.find_element(By.ID, "input_7_9"), in_data.get_zip())

    actions.send_keys_to_element(driver.find_element(By.ID, "input_7_11"), in_data.get_text())

    actions.perform()
    actions.release()

    select_country()
    load_file()

    actions.reset_actions()

    actions.send_keys_to_element(driver.find_element(By.ID, "input_7_17"), in_data.get_text())
    actions.click(driver.find_element(By.XPATH, '/html/body/main/article/div/div/div/div/div/div/form/div[2]/ul/li[13]/div/ul/li/label'))
    actions.click(driver.find_element(By.XPATH, '/html/body/main/article/div/div/div/div/div/div/form/div[3]/input[1]'))

    actions.perform()

def select_country():
    driver.find_element(By.CSS_SELECTOR, "b.button").click()
    driver.find_element(By.CSS_SELECTOR,
                        f".selectric-scroll > ul:nth-child(1) > li:nth-child({random.randrange(2, 249)})").click()


def load_file():
    load_zone = driver.find_element(By.ID, "input_7_12")

    try:
        load_zone.send_keys(CV_PATH)
    except:
        print("error during file upload")
        return


def kill_proc():
    os.system("taskkill /f /im chromedriver.exe")


accept_cookie_policy()
do_careers_navigation()
do_regions_scroll()
search_vacancy()
select_vacancy()
apply_now()

kill_proc()
