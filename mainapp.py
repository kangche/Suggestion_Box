from flask import Flask
import logging
import sys
from configure import config
sys.path.append(config['global']['root_path'])
from apps import view_noauth as vnoauth
from models.model_ckeditor import ckeditor
from datetime import datetime
from configure import config

log_filename = config['global']['log_path']+'/'+datetime.now().strftime("app_%Y-%m-%d.log")
logging.basicConfig(filename=log_filename, level=logging.DEBUG)

def creat_app():
    app = Flask(__name__)
    app.secret_key = config['flask11']['apikey']
    app.register_blueprint(vnoauth.noauth)
    ckeditor.init_app(app)
    app.config['CKEDITOR_PKG_TYPE'] = config['flask11']['ckeditor_pkg']
    app.config['CKEDITOR_SERVE_LOCAL'] = True
    app.config['CKEDITOR_HEIGHT'] = config['flask11']['ckeditor_height']

    return app