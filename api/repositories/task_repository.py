from api.repositories.base_repository import BaseRepository
from api.models import Task


class TaskRepository(BaseRepository):
    name = "task"
    model = Task