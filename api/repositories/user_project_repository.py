from api.repositories.base_repository import BaseRepository
from api.models import UserProject


class UserProjectRepository(BaseRepository):
    name = "user project"
    model = UserProject

    def filter(
        self,
        user_id=None,
        project_id=None,
        status=None,
        created_by=None,
    ):
        query = self.query

        if user_id:
            query = query.filter(UserProject.user_id == user_id)

        if project_id:
            query = query.filter(UserProject.project_id == project_id)

        if status:
            query = query.filter(UserProject.status == status)

        if created_by:
            query = query.filter(UserProject.created_by == created_by)

        return query.all()
