from tables import BaseModel
from sqlalchemy import Integer, Column, Unicode, DateTime
from marshmallow import Schema, fields


class QuestionSchema(Schema):
    question_id = fields.Integer()
    question = fields.String()
    answer = fields.String()
    create_date = fields.DateTime()


class Questions(BaseModel):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer)
    question = Column(Unicode(500))
    answer = Column(Unicode(255))
    create_date = Column(DateTime)
