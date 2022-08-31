from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import random
import inputDataGen
from paths import *

driver = webdriver.Chrome(DRIVER_PATH)
driver.get(MAIN_PAGE_LINK)
actions = ActionChains(driver)


def accept_cookie_policy():
    if driver.find_element(By.XPATH, COOKIE_CONFIRM_BUTTON):
        driver.find_element(By.XPATH, COOKIE_CONFIRM_BUTTON).click()


def do_careers_navigation():
    menu = driver.find_element(By.XPATH, NAV_BAR_PATH)
    company_submenu = driver.find_element(By.XPATH, COMPANY_SUBMENU)
    company_careers_submenu = driver.find_element(By.XPATH, COMPANY_CAREERS_SUBMENU)

    actions.move_to_element(menu)
    actions.move_to_element(company_submenu)
    actions.click(company_careers_submenu)
    actions.perform()


def do_regions_scroll():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    regions_block = driver.find_element(By.XPATH, REGIONS_BLOCK)
    cord = regions_block.location.values()

    driver.execute_script(f"window.scroll({cord.mapping.get('x')}, {cord.mapping.get('y')});")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, LATIN_AMERICA_IMG)))
    regions_block.find_element(By.XPATH, LATIN_AMERICA_IMG).click()


def search_vacancy():
    search_field = driver.find_element(By.XPATH, SEARCH_FIELD)
    search_field.click()
    actions.send_keys_to_element(search_field, SEARCH_REQUEST_BODY).send_keys(Keys.ENTER).perform()


def select_vacancy():
    try:
        nec_vacancy = driver.find_element(By.PARTIAL_LINK_TEXT, SEARCH_REQUEST_BODY)
    except NoSuchElementException:
        print(SEARCH_ERROR_MSG)
        return

    nec_vacancy.click()


def apply_now():
    in_data = inputDataGen.InputFieldGenerator()
    full_name = in_data.get_full_name()

    driver.find_element(By.XPATH, APPLY_BUTTON).click()

    actions.send_keys_to_element(driver.find_element(By.XPATH, FIRSTNAME), full_name[0])
    actions.send_keys_to_element(driver.find_element(By.XPATH, LASTNAME), full_name[1])

    actions.send_keys_to_element(driver.find_element(By.XPATH, EMAIL), in_data.get_email())
    actions.send_keys_to_element(driver.find_element(By.XPATH, PHONE), in_data.get_phone())
    actions.send_keys_to_element(driver.find_element(By.XPATH, STATE), in_data.get_state())
    actions.send_keys_to_element(driver.find_element(By.XPATH, CITY), in_data.get_city())
    actions.send_keys_to_element(driver.find_element(By.XPATH, ZIP), in_data.get_zip())

    actions.send_keys_to_element(driver.find_element(By.XPATH, SKILL_SUMMARY), in_data.get_text())

    actions.perform()
    actions.release()

    select_country()
    load_file()

    actions.reset_actions()

    actions.send_keys_to_element(driver.find_element(By.XPATH, ABOUT_US), in_data.get_text())
    actions.click(driver.find_element(By.XPATH, SAVE_INFO_CHECKBOX))
    actions.click(driver.find_element(By.XPATH, SUBMIT_APPLICATION_BUTTON))

    actions.perform()

def select_country():
    driver.find_element(By.XPATH, COUNTRY_BTN).click()
    driver.find_element(By.CSS_SELECTOR,
                        f".selectric-scroll > ul:nth-child(1) > li:nth-child({random.randrange(2, 249)})").click()


def load_file():
    load_zone = driver.find_element(By.XPATH, FILE_LOAD_ZONE)

    try:
        load_zone.send_keys(CV_PATH)
    except:
        print(FILE_ERROR_MSG)
        return


def kill_proc():
    os.system(KILL_PROC_CMD)


accept_cookie_policy()
do_careers_navigation()
do_regions_scroll()
search_vacancy()
select_vacancy()
apply_now()

kill_proc()
