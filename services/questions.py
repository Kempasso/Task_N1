import json
from dataclasses import dataclass
from typing import Union, Any

import requests

from config import QUESTIONS_API
from repositories import questions_repo, QuestionsRepo
from tables import Questions


@dataclass
class QuestionsService:
    repo: QuestionsRepo = questions_repo
    external_api: str = QUESTIONS_API

    def get_last_question(self) -> Union[Questions, bool]:
        last_question_instance = self.repo.get_last()
        if not last_question_instance:
            return False
        return last_question_instance

    def create_question_in_db(self, **kwargs: Any) -> Questions:
        question_instance = self.repo.create(**kwargs)
        return question_instance

    def some(self, questions: list[dict]):
        for question in questions:
            check_result = self.check_exist_question(question)
            if not check_result:
                while not check_result:
                    new_question = self.get_questions_from_external_api()[0]
                    check_result = self.check_exist_question(new_question)

    def check_exist_question(self, question: dict) -> Union[Questions, bool]:
        check_instance = self.repo.get_by_values(question_id=question['id'])

        if check_instance:
            return False
        else:
            return self.create_question_in_db(question_id=question['id'],
                                              question=question['question'],
                                              answer=question['answer'],
                                              create_date=question['created_at']
                                              )

    def get_questions_from_external_api(self, count: int = 1) -> list[dict]:
        questions = requests.get(f"{self.external_api}{count}").json()
        return questions
