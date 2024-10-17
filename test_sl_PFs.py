import pytest
import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as EC


chromedriver_autoinstaller.install()


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.get('https://petfriends.skillfactory.ru/login')
    driver.maximize_window()
    driver.find_element(By.ID, 'email').send_keys('nikitin@mail.com')
    driver.find_element(By.ID, 'pass').send_keys('74698525')
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    yield driver
    driver.quit()


def test_show_all_pets(driver):

   assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"


def test_show_all_my_pets(driver):

    time.sleep(2)
    wdw(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//a[text()="Мои питомцы"]')))
    driver.find_element(By.XPATH, '//a[text()="Мои питомцы"]').click()
    driver.implicitly_wait(5)
    pets_number = driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(': ')[1]
    pets_count = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')

    assert int(pets_number) == int(len(pets_count))


def test_photo_pets(driver):

    time.sleep(2)
    wdw(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Мои питомцы"]')))
    driver.find_element(By.XPATH, '//a[text()="Мои питомцы"]').click()
    driver.implicitly_wait(5)
    pets_count = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')
    image_count = driver.find_elements(By.XPATH, '//img[starts-with(@src, "data:image/")]')

    assert int(len(image_count)) >= int(len(pets_count) / 2)


def test_my_pets_have_name_breed_age(driver):

    time.sleep(2)
    wdw(driver, 2).until(EC.presence_of_element_located((By.XPATH, '//a[text()="Мои питомцы"]')))
    driver.find_element(By.XPATH, '//a[text()="Мои питомцы"]').click()

    driver.implicitly_wait(5)
    wdw(driver, 2).until(EC.presence_of_all_elements_located((By.XPATH, '//tbody')))
    names = driver.find_elements(By.XPATH, '//td[1]')
    breeds = driver.find_elements(By.XPATH, '//td[2]')
    ages = driver.find_elements(By.XPATH, '//td[3]')

    for i in range(len(names)):

        assert names[i].text != ''
        assert breeds[i].text != ''
        assert ages[i].text != ''

def test_my_pets_have_different_names(driver):

    time.sleep(2)
    wdw(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Мои питомцы"]')))
    driver.find_element(By.XPATH, '//a[text()="Мои питомцы"]').click()

    driver.implicitly_wait(5)
    names = driver.find_elements(By.XPATH, '//td[1]')
    list_names = []
    for i in range(len(names)):
        list_names.append(names[i].text)
    set_names = set(list_names)
    assert len(list_names) == len(set_names)


def test_my_pets_all_different(driver):

    time.sleep(2)
    wdw(driver, 2).until(EC.presence_of_element_located((By.XPATH, '//a[text()="Мои питомцы"]')))
    driver.find_element(By.XPATH, '//a[text()="Мои питомцы"]').click()

    driver.implicitly_wait(5)
    pets = driver.find_elements(By.XPATH, '//tr')
    all_attributes = []
    for pet in pets:
        attributes = pet.find_element(By.XPATH, '//tr').text.split('\n')
        all_attributes.extend(attributes)

    assert len(all_attributes) == len(set(all_attributes))
