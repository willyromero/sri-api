from flask import current_app
from services.SRIData import SRIData

# def get_sri_data(ruc, timeout):
def get_sri_data(ruc="2390060680001", timeout=10):
    sri_data = SRIData(ruc)
    response = sri_data.create_data(timeout)
    print("response", response)

