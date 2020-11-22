from api.repositories.base_repository import BaseRepository
from api.repositories.user_repository import UserRepository
from api.models import Project, User, UserProject, UserProjectStatusEnum


class ProjectRepository(BaseRepository):
    name = "project"
    model = Project

    def __init__(self, user_repository=UserRepository()):
        self.user_repository = user_repository

    def filter(
        self, user_id=None, project_id=None, status=None, created_by=None
    ):
        query = self.query

        if status:
            query = query.join(
                UserProject, UserProject.project_id == Project.id
            ).filter(UserProject.status == status)

        if user_id:
            user_ids = user_id if isinstance(user_id, list) else [user_id]
            query = query.filter(UserProject.user_id.in_(user_ids))

        if project_id:
            project_ids = (
                project_id if isinstance(project_id, list) else [project_id]
            )
            query = query.filter(Project.id.in_(project_ids))

        if created_by:
            created_by_ids = (
                created_by if isinstance(created_by, list) else [created_by]
            )
            query = query.filter(Project.created_by.in_(created_by_ids))

        return query.all()

    def insert(self, user_id, **kwargs):
        user_project = UserProject(created_by=user_id)
        project = self.model(created_by=user_id, **kwargs)
        user_project.user = self.user_repository.get(user_id)
        user_project.status = "active"
        project.users.append(user_project)
        self.session.add(project)
        self.session.commit()
        self.session.refresh(project)
        return project