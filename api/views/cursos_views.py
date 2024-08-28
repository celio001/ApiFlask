from flask_restful import Resource
from api import api


class CursoList(Resource):
    def get(self):
        return 'Ola mundo'

api.add_resource(CursoList, '/cursos')