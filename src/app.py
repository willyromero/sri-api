from flask import Flask
from routes import home, not_found


app = Flask(__name__)

if __name__ == "__main__":

    # app.config.from_object("config.ProductionConfig")
    app.config.from_object("config.DevelopmentConfig")

    # Blueprints
    app.register_blueprint(home.main, url_prefix="/sri/api/")

    # error page
    app.register_error_handler(404, not_found.page)

    app.run()