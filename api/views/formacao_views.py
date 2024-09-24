from flask_restful import Resource
from api import api
from ..schemas import formacao_schema
from flask import request, make_response, jsonify
from ..entidades import formacao
from ..services import formacao_service


class FormcaoList(Resource):
    def get(self):
        formacoes = formacao_service.listar_formacoes()
        fs = formacao_schema.FormaSchema(many=True)
        return make_response(fs.jsonify(formacoes), 200)
    def post(self):
        fs = formacao_schema.FormaSchema()
        validate = fs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        
        else:
            nome = request.json['nome']
            descricao = request.json['descricao']
    

            novo_formacao = formacao.Formacao(nome=nome, descricao=descricao)
            resultado = formacao_service.cadastrar_formacao(novo_formacao)

            x = fs.jsonify(resultado)
            return make_response(x, 201)

class FormcaoDetail(Resource):
    def get(self, id):
        formacao = formacao_service.lista_formacao_id(id)

        if formacao is None:
            return make_response(jsonify("Formcao não foi encontrado", 404))
        
        fs = formacao_schema.FormaSchema()
        return make_response(fs.jsonify(formacao), 200)


    def put(self, id):
        formacao_bd = formacao_service.lista_formacao_id(id)
        if formacao is None:
            return make_response(jsonify('Formcao não foi encontrado'), 404)
        fs = formacao_schema.FormaSchema()
        validate = fs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            descricao = request.json['descricao']
            novo_formacao = formacao.Formacao(nome=nome, descricao=descricao)
            formacao_service.atualizar_formacao(formacao_bd, novo_formacao)
            formacao_atualizado = formacao_service.lista_formacao_id(id)
            return make_response(fs.jsonify(formacao_atualizado), 200)

    def delete(self, id):
        formacao_bd = formacao_service.lista_formacao_id(id)
        if formacao_bd is None:
            return make_response(jsonify('formacao não encontrado'), 400)
        
        formacao_service.remover_formacao(formacao_bd)
        return make_response(jsonify("Formcao excluido com sucesso"), 204)

api.add_resource(FormcaoList, '/formacoes')
api.add_resource(FormcaoDetail, '/formacoes/<int:id>')