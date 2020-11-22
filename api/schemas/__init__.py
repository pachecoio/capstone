from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields
from datetime import datetime


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
    created_at = fields.DateTime()
    created_by = fields.Integer()
    updated_at = fields.DateTime()

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
    created_at = fields.DateTime(default=datetime.now())
    created_by = fields.Method("build_created_by")

    def build_created_by(self, obj):
        return obj.user_id


class ProjectUpdateSchema(Schema):

    name = fields.String()
    description = fields.String()
    updated_at = fields.DateTime(default=datetime.now())


class TaskSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    description = fields.String()
    project_id = fields.Integer()
    project = fields.Nested(ProjectSchema)
    created_at = fields.DateTime()
    created_by = fields.Integer()
    updated_at = fields.DateTime()


class TaskCreateSchema(Schema):
    name = fields.String(required=True)
    description = fields.String(required=True)
    project_id = fields.Integer(required=True)


class TaskUpdateSchema(Schema):
    name = fields.String()
    description = fields.String()
    updated_at = fields.DateTime(default=datetime.now())


class UserProjectSchema(Schema):
    project = fields.Nested(ProjectSchema)
    user = fields.Nested(UserSchema)
    status = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    created_by = fields.Integer()