def page(err):
    response = {
        "status": "FAILED",
        "data": {"error": "This resource not exists"}
    }
    return response, 404