from flask import Flask
from threading import Lock

from .main import shared_environment_wrapper

class api():
    def __init__(self, environment: shared_environment_wrapper):
        self.environment = environment
        self.lock = Lock()
        app = Flask(__name__, instance_relative_config=True)

        @app.route('/hello')
        def hello():
            with self.lock:
                return 'Hello, World!'
        return app