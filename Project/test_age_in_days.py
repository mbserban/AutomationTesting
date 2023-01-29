from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import pytest


# https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler
# import http.server
# import socketserver
#
# PORT = 8000
#
# Handler = http.server.SimpleHTTPRequestHandler
#
# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print("serving at port", PORT)
#     httpd.serve_forever()

def test_main():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get("http://localhost:8000/Mihaita%20Serban/project/")  # cu metoda get incarcam un url
    driver.implicitly_wait(3)

    # assert "Javascript Challenge" in driver.title  # confirmam ca am ajuns pe pagina buna
    elem = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/button")  # cautam in pagina butonul
    elem.click()  # dam click pe buton
    alert = driver.switch_to.alert
    alert.send_keys("2000")  # scriem textul
    driver.implicitly_wait(10)
    alert.accept()
    # alert.send_keys(Keys.RETURN)  # apasam ENTER
    casuta_rezultat = driver.find_element(By.ID, "ageInDays")  # se identifica casuta
    text_casuta = casuta_rezultat.get_attribute('innerText')  # se preia textul din casuta
    assert text_casuta == "You are 8030 days old."
    driver.close()


if __name__ == '__main__':
    test_main()
