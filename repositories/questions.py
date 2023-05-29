from dataclasses import dataclass

from repositories.base import BaseRepo
from repositories.mixins import CreateMixin, GetMixin
from tables import Questions


@dataclass
class QuestionsRepo(BaseRepo, CreateMixin, GetMixin):
    table = Questions
