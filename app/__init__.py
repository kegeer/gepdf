from flask import Flask, redirect, url_for
from app import config
from app.api.clients import ClientApi
from app.extensions import toobar
from app.models import db
from .controllers import report

# Fix the BUG:
#    UnicodeEncodeError: 'ascii' codec can't encode characters in position
# TS: Set the system encoding to utf-8(support chinese)
# Q: Why need to reload the sys module?
# A: System will be deleted the sys.setdefaultencoding after imported the site.py
#    So, we have to reload the sys module and reset the default encoding again

def create_app(object_name):

    app = Flask(__name__)
    app.config.from_object(object_name)

    db.init_app(app)
    toobar.init_app(app)

    # restful_api.add_resource(
    #     ClientApi,
    #     '/api/clients',
    #     '/api/clients/<string:client_id>',
    #     endpoint='restful_api_post'
    # )

    @app.route('/')
    def index():
        return redirect(url_for('report.home'))

    app.register_blueprint(report.report_blueprint)

    # restful_api.init_app(app)

    return app