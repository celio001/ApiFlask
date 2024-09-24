from api import ma
from ..models import formacao_model
from marshmallow import fields

class FormaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = formacao_model.Formacao
        load_instace = True
        fields = ('id', 'nome', 'descricao')

    nome = fields.String(required=True)
    descricao = fields.String(required=True)
