from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    email = fields.String()


class UserCreateSchema(Schema):
    name = fields.String(required=True)
    email = fields.String(required=True)