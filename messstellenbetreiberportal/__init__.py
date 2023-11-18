from flask import Flask
import os

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from .backend import smartmeter, supplier
    app.register_blueprint(smartmeter.bp)
    app.register_blueprint(supplier.bp)

    from .frontend import smartmeter, supplier, dashboard
    app.register_blueprint(smartmeter.bp)
    app.register_blueprint(supplier.bp)
    app.register_blueprint(dashboard.bp)

    return app