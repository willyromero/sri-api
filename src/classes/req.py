from socket import timeout
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json, time, requests
from webdriver_manager.chrome import ChromeDriverManager
from seleniumwire import webdriver as webdriverwire

import email
import pprint
from io import StringIO

# without interaction
# option = webdriver.ChromeOptions()
# option.add_argument('headless')
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)

# for see interaction
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
# chrome_options = Options()
options.add_experimental_option("detach", True)                         
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver_wire = webdriverwire.Chrome(ChromeDriverManager().install(), options=options)
url_to_grab = "https://srienlinea.sri.gob.ec/sri-en-linea/SriRucWeb/ConsultaRuc/Consultas/consultaRuc/"
driver_wire.get(url_to_grab)

text_imput = driver_wire.find_element(By.ID, "busquedaRucId")
text_imput.send_keys("2390060680001")

consultar_button = WebDriverWait(driver_wire, timeout=5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='row'][2]//button" )))
consultar_button.click()

time.sleep(5)

# print("driver_wire.requests", json.loads(driver_wire.requests))

# all_elements = driver_wire.requests[len(driver_wire.requests) -1]

# auth_header = all_elements.headers

# print("auth", dict(auth_header))


# pop the first line so we only process headers
# _, headers = auth_header.split('\r\n', 1)

# # construct a message from the request string
# message = email.message_from_file(StringIO(headers))

# # construct a dictionary containing the headers
# headers = dict(message.items())

# # pretty-print the dictionary of headers
# pprint.pprint(headers, width=160)

authorization = ""
for request in reversed(driver_wire.requests):
    print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("-------------------------------------------------------------")
    # print("request.url  -->", type(request.url))
    print("request.url  -->", request.url)
    if request.url ==  "https://srienlinea.sri.gob.ec/sri-catastro-sujeto-servicio-internet/rest/ConsolidadoContribuyente/obtenerPorNumerosRuc?&ruc=2390060680001":
        authorization = dict(request.headers)["Authorization"]
        print("request.headers  -->", json.dumps(dict(request.headers)))
        print("auth", authorization)
        break
    # print("-------------------------------------------------------------")
    # print("request.headers  -->", type(request.headers))
    # print("request.response.headers -->", request.response.headers)



## define url to request
url_datos = "https://srienlinea.sri.gob.ec/sri-catastro-sujeto-servicio-internet/rest/ConsolidadoContribuyente/obtenerPorNumerosRuc?&ruc=2390060680001"
url_establecimientos = "https://srienlinea.sri.gob.ec/sri-catastro-sujeto-servicio-internet/rest/Establecimiento/consultarPorNumeroRuc?numeroRuc=2390060680001"

# define dictionary with authorization token
request_headers = {
    "Authorization": str(authorization)
}

# requests to get data
request1 = requests.get(url=url_datos, headers=request_headers)
request2 = requests.get(url=url_establecimientos, headers=request_headers)
# request_text = requests.get(url=url, cookies=request_cookie)
print("request data -----> \n", json.dumps(json.loads(request1.text), indent=1))
print("request establecimientos -----> \n", json.dumps(json.loads(request2.text), indent=1))