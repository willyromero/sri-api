from textwrap import indent
import requests
import json
url_datos = "https://srienlinea.sri.gob.ec/sri-catastro-sujeto-servicio-internet/rest/ConsolidadoContribuyente/obtenerPorNumerosRuc?&ruc=2390060680001"
url_establecimientos = "https://srienlinea.sri.gob.ec/sri-catastro-sujeto-servicio-internet/rest/Establecimiento/consultarPorNumeroRuc?numeroRuc=2390060680001"
request_cookie = {
    "Cookie": "TS01ed1cee=0115ac86d2a132a5601ef6939355a2647bf27acb72f798db8234a0b384ed07f812f2416ca4eb740fac0aa9e9d7ed65a3d761206cf8dc403c6368f844786b4227a96847d013"
}

request_headers = {
    "Authorization": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJERUNMQVJBQ0lPTkVTIiwiaWF0IjoxNjY0ODM3MTQ3LCJzdWIiOiJERUNMQVJBVE9SSUEgUFJFU0NSSVBDSU9OIEhFUkVOQ0lBIiwiZXhwIjoxNjY0ODM3NzQ3fQ.2Zf9opBk_dNpapOhKnUSKvz5qA4Vip1VFXNJrVrMGQI"
}

request1 = requests.get(url=url_datos, headers=request_headers)
request2 = requests.get(url=url_establecimientos, headers=request_headers)
# request_text = requests.get(url=url, cookies=request_cookie)
print("request data -----> \n", json.dumps(json.loads(request1.text), indent=1))
print("request establecimientos -----> \n", json.dumps(json.loads(request2.text), indent=1))