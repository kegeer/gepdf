from flask import abort
from flask_restful import Resource, fields, marshal_with

from app.api import parsers
from app.models import Client


class ResultsApi(Resource):
    def get(self, result_id):
        pass
