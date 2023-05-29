from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

from tables.questions import Questions
from tables.questions import QuestionSchema
