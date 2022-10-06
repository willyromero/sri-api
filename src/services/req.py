import json
import requests 
import time
import glob
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from seleniumwire import webdriver as webdriverwire
# from webdriver_manager.chrome import ChromeDriverManager

curret_path = Path(__file__).parent.resolve() 
cert_path = curret_path / "driver"
driver_path = glob.glob(f"{cert_path}/*.exe")[0]


url_to_grab = "https://srienlinea.sri.gob.ec/sri-en-linea/SriRucWeb/ConsultaRuc/Consultas/consultaRuc/"
ruc = "2390060680001"
url_datos = f"https://srienlinea.sri.gob.ec/sri-catastro-sujeto-servicio-internet/rest/ConsolidadoContribuyente/obtenerPorNumerosRuc?&ruc={ruc}"
url_establecimientos = f"https://srienlinea.sri.gob.ec/sri-catastro-sujeto-servicio-internet/rest/Establecimiento/consultarPorNumeroRuc?numeroRuc={ruc}"

id_ruc_input = "busquedaRucId"
xpath_consultar_button = "//div[@class='row'][2]//button"
xpath_verify = f"//*[text()[contains(.,'{ruc}')]]"

authorization_token = ""

i = 0 

while True:
    max_iteration = 0
# for see interaction
    options = webdriverwire.ChromeOptions()
    options.add_argument('headless')
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    # options.add_argument("--disable-extensions")
    # options.add_argument("--window-size=500, 500")
    # options.add_experimental_option("detach", False)                         

    # driver_wire = webdriverwire.Chrome(ChromeDriverManager().install(), options=options)
    driver_wire = webdriverwire.Chrome(driver_path, options=options)


    driver_wire.get(url_to_grab)
    print("iteration ---> ", i)

    try:    
        ruc_imput = driver_wire.find_element(By.ID, id_ruc_input)
        ruc_imput.send_keys(ruc)

        consultar_button = WebDriverWait(driver_wire, timeout=15).until(EC.element_to_be_clickable((By.XPATH, xpath_consultar_button )))
        consultar_button.click()

        # Elemento html existente en la página con los datos (verifica que se accedio)
        time.sleep(5)

        # print("verify_element", verify_element)
        # verify_element =  driver_wire.find_element(By.XPATH, str(xpath_verify))

        # if verify_element != None:
        for request in reversed(driver_wire.requests):
            max_iteration = max_iteration + 1
            print("req url ", request.url)
            if request.url ==  url_datos:
                authorization_token = dict(request.headers)["Authorization"]
                print("auth ", authorization_token)
                break
        print("max iteration", max_iteration)
    except Exception as err:
        print({"Status": "FAILED", "message":err.args})


    if authorization_token != "":

        # define dictionary with authorization_token
        request_headers = {
            "Authorization": str(authorization_token)
        }

        # requests to get data
        request1 = requests.get(url=url_datos, headers=request_headers)
        request2 = requests.get(url=url_establecimientos, headers=request_headers)
        # print("request data -----> \n", json.dumps(json.loads(request1.text), indent=1))
        print("request establecimientos -----> \n", json.dumps(json.loads(request2.text), indent=1))
    
    i = i + 1
    driver_wire.quit()
    if i == 10:
        break