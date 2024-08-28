from api import ma
from ..models import curso_model
from marshmallow import fields

class CursoSchema(ma.SQLAlchemyAutoSchema):
    model = curso_model.Cursos
    load_instace = True
    fields = ('id', 'nome', 'descricao', 'data_publicacao')

    nome = fields.String(required=True)
    descricao = fields.String(required=True)
    data_publicacao = fields.Date(required=True)