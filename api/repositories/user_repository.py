from api.repositories.base_repository import BaseRepository
from api.models import User


class UserRepository(BaseRepository):
    name = "user"
    model = User