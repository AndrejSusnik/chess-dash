from flask import Flask
from flask.views import MethodView
import marshmallow as ma
from flask_smorest import Api, Blueprint, abort
from flask_cors import CORS
import requests

from pony.orm import select

from models import ParticipantSchema, CategorySchema, ResultsSchema
from db import db, Participant, Category, Results

app = Flask(__name__)
app.config['API_TITLE'] = 'Chess Tournament backend service'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.0.3'
app.config['OPENAPI_URL_PREFIX'] = '/'
app.config['OPENAPI_JSON_PATH'] = 'openapi.json'
app.config['OPENAPI_SWAGGER_UI_PATH'] = '/openapi/'
app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

CORS(app)

api = Api(app)
blp = Blueprint("ChessTournamentService", __name__,
                url_prefix="", description="ChessTournamentService API")


@blp.route("/participants")
class Participants(MethodView):
    @blp.response(200, ParticipantSchema(many=True))
    def get(self):
        return select(p for p in Participant)[:]


api.register_blueprint(blp)

if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0")