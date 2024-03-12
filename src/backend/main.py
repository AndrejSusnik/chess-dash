from flask import Flask
from flask.views import MethodView
from flask_smorest import Api, Blueprint  # type: ignore
from flask_cors import CORS  # type: ignore

from pony.orm import select, db_session

from models import (ParticipantSchema, CategorySchema, ResultSchema,
                    ParticipantPostSchema, ResultPostSchema,
                    CategoryPostSchema, ParticipantQuerySchema,
                    CategoryQuerySchema, ResultQuerySchema)
from db import Participant, Category, Result

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
        with db_session:
            return select(p for p in Participant)[:]


@blp.route("/participant")
class ParticipantView(MethodView):
    @blp.arguments(ParticipantPostSchema)
    @blp.response(201, ParticipantSchema)
    def post(self, participant):
        with db_session:
            p = Participant(**participant)
            return p.to_dict()

    @blp.arguments(ParticipantSchema)
    @blp.response(200, ParticipantSchema)
    def put(self, participant):
        with db_session:
            p = Participant[participant['id']]
            p.set(**participant)
            return p.to_dict()

    @blp.arguments(ParticipantQuerySchema)
    @blp.response(204)
    def delete(self, participant):
        with db_session:
            p = Participant[participant['id']]
            p.delete()


@blp.route("/categories")
class Categories(MethodView):
    @blp.response(200, CategorySchema(many=True))
    def get(self):
        with db_session:
            return select(c for c in Category)[:]


@blp.route("/category")
class CategoryView(MethodView):
    @blp.arguments(CategoryPostSchema)
    @blp.response(201, CategorySchema)
    def post(self, category):
        with db_session:
            c = Category(**category)
            return c.to_dict()

    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    def put(self, category):
        with db_session:
            c = Category[category['id']]
            c.set(**category)
            return c.to_dict()

    @blp.arguments(CategoryQuerySchema)
    @blp.response(204)
    def delete(self, category):
        with db_session:
            c = Category[category['id']]
            c.delete()


@blp.route("/results")
class Results(MethodView):
    @blp.response(200, ResultSchema(many=True))
    def get(self):
        with db_session:
            return select(r for r in Result)[:]


@blp.route("/result")
class ResultView(MethodView):
    @blp.arguments(ResultPostSchema)
    @blp.response(201, ResultSchema)
    def post(self, result):
        with db_session:
            p1 = Participant[result['participant1']['id']]
            p2 = Participant[result['participant2']['id']]
            c = Category[result['category']['id']]
            r = Result(result=result['result'], participants=[p1, p2])
            r.participants.add(p2)
            r.categories.add(c)
            return r.to_dict()

    @blp.arguments(ResultSchema)
    @blp.response(200, ResultSchema)
    def put(self, result):
        with db_session:
            r = Result[result['id']]
            p1 = Participant[result['participant1']['id']]
            p2 = Participant[result['participant2']['id']]
            c = Category[result['category']['id']]
            r.set(result=result['result'])
            r.participants.clear()
            r.participants.add(p1)
            r.participants.add(p2)
            r.categories.clear()
            r.categories.add(c)
            return r.to_dict()

    @blp.arguments(ResultQuerySchema)
    @blp.response(204)
    def delete(self, result):
        with db_session:
            r = Result[result['id']]
            r.delete()


api.register_blueprint(blp)

if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0")
