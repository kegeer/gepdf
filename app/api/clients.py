from flask import abort
from flask_restful import Resource, fields, marshal_with

from app.api import parsers
from app.models import Client

client_fields = {
    'source': fields.String,
    'name': fields.String,
    'phone_num': fields.String,
    'puyuan_id': fields.String,
    'original_id': fields.String,
    'gender': fields.Integer,
    'age': fields.Integer,
    'height': fields.Float,
    'weight': fields.Float,
    'bmi': fields.Float,
    'inspector': fields.Integer,
    'auditor': fields.Integer,
    'smoke': fields.Boolean,
    'drink': fields.Boolean,
    'sampling_date': fields.DateTime,
    'receive_date': fields.DateTime,
    'inspect_date': fields.DateTime,
    'report_date': fields.DateTime,
    'report': fields.Boolean,
    'triglyceride': fields.Float,
    'cholesterol': fields.Float,
    'h_lipoprotein': fields.Float,
    'l_lipoprotein': fields.Float,
    'fbg': fields.Float,
    'defecate': fields.Integer,
    'medical_history': fields.String,
    'family_history': fields.String,
    'medicine': fields.String,
    'remarks': fields.String
}

class ClientApi(Resource):
    @marshal_with(client_fields)
    def get(self, client_id=None):
        if client_id:
            client = Client.query.filter_by(id=client_id).first()
            if not client:
                abort(404)
            return client
        else:
            args = parsers.client_get_parser.parse_args()
            # page = args['page'] or 1

            clients = Client.query.all()
            # ).paginate(page, 30)
            return clients
    def post(self, post_id=None):
        pass
