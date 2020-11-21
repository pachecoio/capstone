from flask import Blueprint, jsonify
from api.repositories.user_repository import UserRepository
from decorators import marshal_with, parse_with
from api.schemas import UserSchema, UserCreateSchema
from auth import requires_auth

blueprint = Blueprint("api_blueprint", __name__)


user_repository = UserRepository()


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
