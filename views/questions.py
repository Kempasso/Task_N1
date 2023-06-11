import requests as requests
from flask import request
from flask_restx import Resource, Namespace

from config import QUESTIONS_API
from services import questions_service
from tables import QuestionSchema
from marshmallow import Schema

questions_namespace = Namespace('')

question_schema: Schema = QuestionSchema()


@questions_namespace.route('/questions')
class QuestionsView(Resource):

    def post(self):
        data = request.json
        questions_count = data.get("questions_num", None)
        if len(data) == 1:
            if not questions_count:
                return {"msg": "Request bad format"}, 401
            elif not isinstance(questions_count, int):
                return {"msg": "Bad type of value"}, 401
        else:
            return {"msg": "Count of values not exact"}, 401

        last_question = questions_service.get_last_question()
        questions = questions_service.get_questions_from_external_api(count=questions_count)

        questions_service.iteration_by_questions(questions)
        if last_question:
            return question_schema.dump(last_question), 200
        return {}
