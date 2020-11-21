from sqlalchemy import (
    Column,
    String,
    Integer,
    create_engine,
    DateTime,
    ForeignKey,
    Table,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from settings import DATABASE_PATH
import json
import os
from datetime import datetime

database_name = "capstone"
database_path = os.environ.get(
    "DATABASE_URL",
    "postgres://{}/{}".format("postgres:root@localhost:5432", database_name),
)

db = SQLAlchemy()

"""
setup_db(app)
    binds a flask application and a SQLAlchemy service
"""


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path or DATABASE_PATH
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

    return db


class TimestampMixin(object):
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    created_by = Column(Integer)


class UserProject(db.Model, TimestampMixin):
    __tablename__ = "user_projects"

    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True
    )
    project_id = Column(
        Integer,
        ForeignKey("projects.id", ondelete="CASCADE"),
        primary_key=True,
    )
    project = relationship("Project", back_populates="users")
    user = relationship("User", back_populates="projects")


class User(db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    picture = Column(String)
    projects = relationship(
        "UserProject",
        back_populates="user",
        cascade="all, delete",
        passive_deletes=True,
    )


class Task(db.Model, TimestampMixin):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    project_id = Column(Integer, ForeignKey("projects.id"))


class Project(db.Model, TimestampMixin):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    tasks = relationship(
        "Task",
        cascade="all, delete",
        passive_deletes=True,
    )
    users = relationship(
        "UserProject",
        back_populates="project",
        cascade="all, delete",
        passive_deletes=True,
    )
