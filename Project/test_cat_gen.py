from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import pytest
import unittest


def test_main():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get("http://localhost:8000/Mihaita%20Serban/project/")  # cu metoda get incarcam un url
    driver.implicitly_wait(3)

    assert "Javascript Challenge" in driver.title  # confirmam ca am ajuns pe pagina buna
    elem = driver.find_element(By.ID, "cat-generator")  # cautam in pagina
    # elem.clear()  # curatam continutul casutei
    # elem.send_keys("pycon")  # scriem textul pyton
    # elem.send_keys(Keys.RETURN)  # apasam ENTER pe casuta

    for i in range(6):
        elem.click()
        driver.implicitly_wait(30)
    # available = len(WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.ID, "//h2[contains(., 'List')]//preceding::div[1]//div[@alt='Closed']"))))
    div = driver.find_element(By.ID, "flex-cat-gen")
    res = list(div.find_elements(By.TAG_NAME, 'img'))
    assert len(res) == 6

    # assert "No results  found." not in driver.page_source  # confirmam ca avem rezultate
    driver.implicitly_wait(30)
    driver.close()  # inchidem fereastra de browser


if __name__ == '__main__':
    test_main()
