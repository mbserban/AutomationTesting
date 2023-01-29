from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import unittest


class TestRock():
    def test_something(self):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver.get("http://localhost:8000/Mihaita%20Serban/project/")  # cu metoda get incarcam un url
        self.driver.implicitly_wait(3)
        assert "Javascript Challenge" in self.driver.title  # confirmam ca am ajuns pe pagina buna
        self.elem = self.driver.find_element(By.ID, "rock")
        self.elem.click()
        self.my_choice = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/img")
        self.my_choice_value = self.my_choice.get_attribute('src')
        self.message = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/h1")
        self.message_value = self.message.get_attribute('innerText')
        self.bot_choice = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/img")
        self.bot_choice_value = self.bot_choice.get_attribute('src')
        if self.my_choice_value == self.bot_choice_value:
            assert self.message_value == "You tied!"
        elif self.bot_choice_value == "data:image/jpeg;base64,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":
            assert self.message_value == "You won!"
        else:
            assert self.message_value == "You lost!"
        self.driver.close()  # inchidem fereastra de browser


if __name__ == '__main__':
    TestRock()
