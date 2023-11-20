from flask import Flask, request
from threading import Lock

from .main import shared_environment_wrapper

class api():
    def __init__(self, environment: shared_environment_wrapper):
        self.environment = environment
        self.lock = Lock()
        app = Flask(__name__, instance_relative_config=True)

        @app.route('/temperature')
        def temperature():
            width = request.args.get('width')
            height = request.args.get('height')
            with self.lock:
                return self.environment.temperature[width][height]

        @app.route('/wind')
        def wind():
            width = request.args.get('width')
            height = request.args.get('height')
            with self.lock:
                return self.environment.wind[width][height]

        @app.route('/sun')
        def sun():
            width = request.args.get('width')
            height = request.args.get('height')
            with self.lock:
                return self.environment.sun[width][height]

        @app.route('/rain')
        def rain():
            width = request.args.get('width')
            height = request.args.get('height')
            with self.lock:
                return self.environment.rain[width][height]

        @app.route('/timestamp')
        def timestamp():
            with self.lock:
                return self.environment.timestamp
            

        return app