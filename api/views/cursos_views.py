from flask_restful import Resource
from api import api
from ..schemas import curso_schema
from flask import request, make_response, jsonify
from ..entidades import curso
from ..services import curso_service


class CursoList(Resource):
    def get(self):
        cursos = curso_service.listar_cursos()
        cs = curso_schema.CursoSchema(many=True)
        return make_response(cs.jsonify(cursos), 200)
    
    def post(self):
        cs = curso_schema.CursoSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        
        else:
            nome = request.json['nome']
            descricao = request.json['descricao']
            data_publicacao = request.json['data_publicacao']

            novo_curso = curso.Curso(nome=nome, descricao=descricao, data_publicacao=data_publicacao)
            resultado = curso_service.cadastrar_curso(novo_curso)

            x = cs.jsonify(resultado)
            return make_response(x, 201)

class CursoDetail(Resource):
    def get(self, id):
        curso = curso_service.lista_curso_id(id)

        if curso is None:
            return make_response(jsonify("Curso não foi encontrado", 404))
        
        cs = curso_schema.CursoSchema()
        return make_response(cs.jsonify(curso), 200)


    def put(self, id):
        curso_bd = curso_service.lista_curso_id(id)
        if curso is None:
            return make_response(jsonify('Curso não foi encontrado'), 404)
        cs = curso_schema.CursoSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            descricao = request.json['descricao']
            data_publicacao = request.json['data_publicacao']
            novo_curso = curso.Curso(nome=nome, descricao=descricao, data_publicacao=data_publicacao)
            curso_service.atualizar_curso(curso_bd, novo_curso)
            curso_atualizado = curso_service.lista_curso_id(id)
            return make_response(cs.jsonify(curso_atualizado), 200)

    def delete(self, id):
        curso_bd = curso_service.lista_curso_id(id)
        if curso_bd is None:
            return make_response(jsonify('Curso não encontrado'), 400)
        
        curso_service.remover_curso(curso_bd)
        return make_response(jsonify("Curso excluido com sucesso"), 204)

api.add_resource(CursoList, '/cursos')
api.add_resource(CursoDetail, '/cursos/<int:id>')