import requests as requests
from flask import request
from flask_restx import Resource, Namespace

from config import QUESTIONS_API
from services import questions_service
from tables import QuestionSchema

questions_namespace = Namespace('')

question_schema = QuestionSchema()


@questions_namespace.route('/questions')
class QuestionsView(Resource):

    def post(self):
        data = request.json
        last_question = questions_service.get_last_question()
        questions = questions_service.get_questions_from_external_api(count=data["questions_num"])

        questions_service.some(questions)
        if last_question:
            return question_schema.dump(last_question), 200
        return {}
