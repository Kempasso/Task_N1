from flask import Flask

from flask_restx import Api

from views.questions import questions_namespace
from config import Config
from repositories import create_t


def create_app(config: Config) -> Flask:
    application: Flask = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    return application


def configure_app(application):
    api = Api(application)
    api.add_namespace(questions_namespace)


if __name__ == '__main__':
    configs = Config()
    app = create_app(configs)
    configure_app(app)
    create_t()
    app.run(debug=True, host='0.0.0.0', port=8000)