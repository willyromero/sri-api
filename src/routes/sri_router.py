from controllers import sri_data_controller
from flask import Blueprint, request
# from .middlewares import request_validator


main = Blueprint("sri", __name__)


@main.route("<ruc>")
def get_person_data(ruc):
    try:
        request_key = request.json["user_key"]

        if True:
            timeout = 10

            if (timeout == None or isinstance(timeout, int)):
                person_data = sri_data_controller.get_sri_data(ruc, timeout)
            else:
                return {
                    "status": "FAILED",
                    "data": {"error": "Default timeout must be number or None value"}
                }

            return person_data
        else:
            return {
                "status": "FAILED",
                "data": {"error": "You can't use this endpoint, unauthorized"}
            }
    except:
        return {
            "status": "FAILED",
            "data": {"error": "You must provide a password"}
        }
