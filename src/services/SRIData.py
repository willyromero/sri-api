import requests
from flask import current_app
from app import return_app
from .Robot import Robot

app = return_app()

class SRIData:
    # url = f"{current_app.config['SCRAP_URL']}"

    # # "//div/input[@placeholder='1700000000001']"
    # ruc_input_xpath = f"{current_app.config['RUC_INPUT_XPATH']}"

    # # "//div[@class='row'][2]//button"
    # consultar_button_xpath = f"{current_app.config['CONSULTAR_BUTTON_XPATH']}"
    with app.app_context():
        robot = Robot(
            scrap_url="https://srienlinea.sri.gob.ec/sri-en-linea/SriRucWeb/ConsultaRuc/Consultas/consultaRuc/",
            ruc_input_xpath=current_app.config['RUC_INPUT_XPATH'],
            consultar_button_xpath=current_app.config['CONSULTAR_BUTTON_XPATH']
        )

        # f"https://srienlinea.sri.gob.ec/sri-catastro-sujeto-servicio-internet/rest/ConsolidadoContribuyente/obtenerPorNumerosRuc?&ruc={ruc}"
        taxpayer_data_url = f"{current_app.config['URL_DATOS']}"

        # f"https://srienlinea.sri.gob.ec/sri-catastro-sujeto-servicio-internet/rest/Establecimiento/consultarPorNumeroRuc?numeroRuc={ruc}"
        establishment_data_url = f"{current_app.config['URL_DATOS_EST']}"

    def __init__(self, ruc):
        self.ruc = ruc  # "2390060680001"

        self.taxpayer_data_url = f"{self.get_taxpayer_data_url()}{self.get_ruc()}"

        self.establishment_data_url = f"{self.get_establishment_data_url*()}{self.get_ruc()}"

    def set_ruc(self, ruc):
        self.ruc = ruc

    def get_ruc(self):
        return self.ruc

    def set_robot(self, robot):
        self.robot = robot

    def get_robot(self):
        return self.robot

    def set_existe_ruc_url(self, url):
        self.existe_ruc_url = url

    def get_existe_ruc_url(self):
        return self.existe_ruc_url

    def set_taxpayer_data_url(self, url):
        self.taxpayer_data_url = url

    def get_taxpayer_data_url(self):
        return self.taxpayer_data_url

    def set_establishment_data_url(self, url):
        self.establishment_data_url = url

    def get_establishment_data_url(self):
        return self.establishment_data_url

    def request_taxpayer_data(self, request_headers, timeout):
        try:
            taxpaper_data = requests.get(
                url=self.get_taxpayer_data_url(),
                timeout=timeout,
                headers=request_headers
            )
            return taxpaper_data
        except Exception as err:
            return {
                "status": "FAILED",
                "data": {"error": err.args}
            }

    def request_establishment_data(self, request_headers, timeout):
        try:
            taxpaper_data = requests.get(
                url=self.get_establishment_data_url(),
                timeout=timeout,
                headers=request_headers
            )
            return taxpaper_data
        except Exception as err:
            return {
                "status": "FAILED",
                "data": {"error": err.args}
            }

    def create_data(self, timeout):
        robot_response = Robot.request_authorization_token(
            taxpayer_data_url=self.get_taxpayer_data_url(),
            ruc=self.get_ruc()
        )

        if robot_response["success"]:
            request_headers = {
                "Authorization": robot_response["token"]
            }
            response = {
                "status": "SUCCESS",
                "data": {
                    "taxpayer": {
                        self.request_taxpayer_data(
                            request_headers=request_headers,
                            timeout=timeout
                        )
                    },
                    "establishment": {
                        self.request_establishment_data(
                            request_headers=request_headers,
                            timeout=timeout
                        )
                    }
                }
            }
            return response
        else:
            response = {
                "status": "FAILED",
                "data": {"message": "Robot cannot get token"}
            }

            return response
