from flask import Flask
from routes import not_found, sri_router


app = Flask(__name__)

def return_app():
    return app


if __name__ == "__main__":

    # app.config.from_object("config.ProductionConfig")
    app.config.from_object("config.DevelopmentConfig")

    # Blueprints
    app.register_blueprint(sri_router.main, url_prefix="/sri/api/")

    # error page
    app.register_error_handler(404, not_found.page)

    app.run()
