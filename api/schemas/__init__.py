from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    email = fields.String()
    picture = fields.String()


class UserCreateSchema(Schema):
    name = fields.String(required=True)
    email = fields.String(required=True)
    picture = fields.String()


class ProjectSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    users = fields.Method("build_users_list")

    def build_users_list(self, obj):
        return [
            {
                "id": user_project.user.id,
                "name": user_project.user.name,
                "email": user_project.user.email,
                "picture": user_project.user.picture,
            }
            for user_project in obj.users
        ]


class ProjectCreateSchema(Schema):

    name = fields.String()
    description = fields.String()
    user_id = fields.Integer()


class ProjectUpdateSchema(Schema):

    name = fields.String()
    description = fields.String()