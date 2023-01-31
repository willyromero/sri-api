import glob
from pathlib import Path
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from seleniumwire import webdriver as webdriverwire


class Robot:

    driver_path = ""

    authorization_token = {
        "success": False,
        "token": ""
    }

    driver = None

    def __init__(self, scrap_url, ruc_input_xpath, consultar_button_xpath):
        # "https://srienlinea.sri.gob.ec/sri-en-linea/SriRucWeb/ConsultaRuc/Consultas/consultaRuc/"
        self.url = scrap_url

        # "//div/input[@placeholder='1700000000001']"
        self.ruc_input_xpath = ruc_input_xpath

        # "//div[@class='row'][2]//button"
        self.consultar_button_xpath = consultar_button_xpath

    def set_url(self, url):
        self.url = url

    def get_url(self):
        return self.url

    def set_ruc_input_xpath(self, xpath):
        self.ruc_input_xpath = xpath

    def get_ruc_input_xpath(self):
        return self.ruc_input_xpath

    def set_consultar_button_xpath(self, xpath):
        self.consultar_button_xpath = xpath

    def get_consultar_button_xpath(self):
        return self.consultar_button_xpath

    def set_driver_path(self, driver_path):
        self.driver_path = driver_path

    def get_driver_path(self):
        return self.driver_path

    def set_authorization_token(self, authorization_token):
        self.authorization_token = authorization_token

    def get_authorization_token(self):
        return self.authorization_token

    def set_driver(self, driver):
        self.driver = driver

    def get_driver(self):
        return self.driver

    def search_driver_path(self):
        curret_path = Path(__file__).parent.resolve()
        cert_path = curret_path / "driver"
        driver_path = glob.glob(f"{cert_path}/*.exe")[0]
        self.set_driver_path(driver_path)

    def create_driver(self):
        self.search_driver_path()

        # set up webdriver (seleniumwiere) options
        options = webdriverwire.ChromeOptions()
        options.add_argument('headless')
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")

        self.set_driver(
            webdriverwire.Chrome(self.get_driver_path(), options=options)
        )

    def request_authorization_token(self, taxpayer_data_url, ruc):
        self.create_driver()
        driverwire = self.get_driver()

        try:
            # set ruc on service
            ruc_imput = driverwire.find_element(
                By.ID, self.get_ruc_input_xpath()
            )
            ruc_imput.send_keys(ruc)

            # wait for button state be enable to click
            consultar_button = WebDriverWait(driverwire, timeout=15).until(
                EC.element_to_be_clickable(
                    (By.XPATH, self.get_consultar_button_xpath())
                )
            )
            consultar_button.click()

            # wait for request  receive more headers data
            time.sleep(5)

            # search for header with authorization token
            for request in reversed(driverwire.requests):
                if request.url == taxpayer_data_url:
                    authorization_token = dict(request.headers)[
                        "Authorization"]
                    self.set_authorization_token(
                        {
                            "success": True,
                            "token": authorization_token
                        }
                    )
                    break

            self.driver.quit()
        except Exception as err:
            print("Error on Robot request_authorization_token", err.args)
