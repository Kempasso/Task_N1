from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URI

from repositories.questions import QuestionsRepo
from tables import BaseModel

engine = create_engine(DATABASE_URI)
session_maker = sessionmaker(engine)

questions_repo = QuestionsRepo(engine=engine, session_maker=session_maker)


def create_t():
    BaseModel.metadata.create_all(engine)
