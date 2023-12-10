from flask import Flask
import os
import logging

logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)

def create_app():
    logger.info("Starting Flask app...")
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    
    logger.info("Registering Backend Blueprints...")
    from .backend import smartmeter, supplier
    app.register_blueprint(smartmeter.bp)
    app.register_blueprint(supplier.bp)

    logger.info("Registering Frontend Blueprints...")
    from .frontend import smartmeter, supplier, dashboard
    app.register_blueprint(smartmeter.bp)
    app.register_blueprint(supplier.bp)
    app.register_blueprint(dashboard.bp)

    return app