from flask import Blueprint, jsonify
from api.repositories.user_repository import UserRepository
from api.repositories.project_repository import ProjectRepository
from api.repositories.task_repository import TaskRepository
from api.repositories.user_project_repository import UserProjectRepository
from decorators import marshal_with, parse_with, parse_request, Argument
from api.schemas import (
    UserSchema,
    UserCreateSchema,
    ProjectSchema,
    ProjectCreateSchema,
    ProjectUpdateSchema,
    TaskSchema,
    TaskCreateSchema,
    TaskUpdateSchema,
    UserProjectSchema,
)
from auth import requires_auth
from api.models import User, UserProject, UserProjectStatusEnum
from datetime import datetime

blueprint = Blueprint("api_blueprint", __name__)


user_repository = UserRepository()
project_repository = ProjectRepository()
task_repository = TaskRepository()
user_project_repository = UserProjectRepository()


# Users


@blueprint.route("/api/user", methods=["GET"])
@requires_auth(permission="get:users")
@marshal_with(UserSchema(many=True))
def get_users(*args, **kwargs):
    return user_repository.query.all()


@blueprint.route("/api/user", methods=["POST"])
@requires_auth(permission="post:users")
@parse_with(UserCreateSchema())
@marshal_with(UserSchema())
def create_user(entity, payload):
    return user_repository.insert(**entity)


@blueprint.route("/api/user", methods=["PATCH"])
@requires_auth(permission="post:users")
@parse_with(UserCreateSchema())
@marshal_with(UserSchema())
def create_or_return_existing_user(entity, payload):
    user = user_repository.query.filter(User.email == entity["email"]).first()
    if user:
        return user_repository.update(id=user.id, **entity)
    return user_repository.insert(**entity)


@blueprint.route("/api/user/<int:id>", methods=["PUT"])
@requires_auth(permission="put:users")
@parse_with(UserSchema())
@marshal_with(UserSchema())
def update_user(entity, payload, id):
    return user_repository.update(id, **entity)


@blueprint.route("/api/user/<int:id>", methods=["DELETE"])
@requires_auth(permission="put:users")
def delete_user(payload, id):
    user_repository.delete(id)
    return jsonify(
        {
            "success": True,
            "error": False,
            "deleted": 1,
        }
    )


# Projects


@blueprint.route("/api/project", methods=["GET"])
@requires_auth(permission="get:users")
@parse_request(
    [
        Argument(name="status"),
        Argument(name="project_id", type=int, append=True),
        Argument(name="user_id", type=int, append=True),
        Argument(name="created_by", type=int, append=True),
    ]
)
@marshal_with(ProjectSchema(many=True))
def get_projects(*args, **kwargs):
    return project_repository.filter(**kwargs)


@blueprint.route("/api/project", methods=["POST"])
@requires_auth(permission="post:users")
@parse_with(ProjectCreateSchema())
@marshal_with(ProjectSchema())
def create_project(entity, payload):
    return project_repository.insert(**entity)


@blueprint.route("/api/project/<int:id>", methods=["PUT"])
@requires_auth(permission="put:users")
@parse_with(ProjectUpdateSchema())
@marshal_with(ProjectSchema())
def update_project(entity, payload, id):
    return project_repository.update(id, updated_at=datetime.now(), **entity)


@blueprint.route("/api/project/<int:id>", methods=["DELETE"])
@requires_auth(permission="delete:users")
def delete_project(payload, id):
    project_repository.delete(id)
    return jsonify(
        {
            "success": True,
            "error": False,
            "deleted": 1,
        }
    )


# Tasks


@blueprint.route("/api/task", methods=["GET"])
@requires_auth(permission="get:users")
@marshal_with(TaskSchema(many=True))
def get_tasks(*args, **kwargs):
    tasks = task_repository.query.all()
    return tasks


@blueprint.route("/api/task", methods=["POST"])
@requires_auth(permission="post:users")
@parse_with(TaskCreateSchema())
@marshal_with(TaskSchema())
def create_task(entity, payload):
    return task_repository.insert(**entity)


@blueprint.route("/api/task/<int:id>", methods=["PUT"])
@requires_auth(permission="PUT:users")
@parse_with(TaskUpdateSchema())
@marshal_with(TaskSchema())
def update_task(entity, payload, id):
    return task_repository.update(id, updated_at=datetime.now(), **entity)


# User projects


@blueprint.route("/api/project/subscriptions", methods=["GET"])
@requires_auth(permission="get:users")
@parse_request(
    [
        Argument(name="status"),
        Argument(name="user_id", type=int),
        Argument(name="project_id", type=int),
        Argument(name="created_by", type=int),
    ]
)
@marshal_with(UserProjectSchema(many=True))
def get_projects_subscriptions(*args, **kwargs):
    return user_project_repository.filter(**kwargs)


@blueprint.route("/api/user/<int:user_id>/projects", methods=["GET"])
@requires_auth(permission="get:users")
@parse_request(
    [
        Argument(name="status"),
        Argument(name="project_id", type=int, append=True),
        Argument(name="created_by", type=int, append=True),
    ]
)
@marshal_with(ProjectSchema(many=True))
def get_user_projects(*args, user_id, **kwargs):
    return project_repository.filter(user_id=user_id, **kwargs)
