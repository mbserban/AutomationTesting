from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import unittest


class TestButtons():
    def test_something(self):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver.get("http://localhost:8000/Mihaita%20Serban/project/")  # cu metoda get incarcam un url
        self.driver.implicitly_wait(3)
        assert "Javascript Challenge" in self.driver.title  # confirmam ca am ajuns pe pagina buna

        self.elem = self.driver.find_element(By.ID, "background")
        self.elem.click()
        self.elem = self.driver.find_element(By.XPATH, '//*[@id="background"]/option[2]')
        self.elem.click()

        self.button_colour = []
        self.buttons = self.driver.find_elements(By.TAG_NAME, "button")
        for i in range(len(self.buttons)):
            self.button_colour.append(self.buttons[i].get_attribute('class'))
        print(self.button_colour)
        for i in self.button_colour:
            assert i == 'btn btn-danger'

        self.driver.close()  # inchidem fereastra de browser


if __name__ == '__main__':
    TestButtons()
