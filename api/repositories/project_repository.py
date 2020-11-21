from api.repositories.base_repository import BaseRepository
from api.repositories.user_repository import UserRepository
from api.models import Project, User, UserProject


class ProjectRepository(BaseRepository):
    name = "project"
    model = Project

    def __init__(self, user_repository=UserRepository()):
        self.user_repository = user_repository

    def insert(self, user_id, **kwargs):
        user_project = UserProject(created_by=user_id)
        project = self.model(**kwargs)
        user_project.user = self.user_repository.get(user_id)
        project.users.append(user_project)
        self.session.add(project)
        self.session.commit()
        self.session.refresh(project)
        return project