import typing
from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker


@dataclass
class BaseMixin:
    table: typing.Any
    engine: Engine
    session_maker: sessionmaker


@dataclass
class CreateMixin(BaseMixin):
    def create(self, **kwargs):
        with self.session_maker() as session:
            new_obj = self.table(**kwargs)
            session.add(new_obj)
            session.commit()
        return new_obj

    def delete(self, **kwargs):
        with self.session_maker() as session:
            res = session.query(self.table).filter_by(**kwargs).first()
            session.delete(res)
            session.commit()


@dataclass
class GetMixin(BaseMixin):

    def get_by_values(self, **kwargs):
        with self.session_maker() as session:
            query = session.query(self.table).filter_by(**kwargs)
            result = query.all()
            return result

    def get_last(self):
        query = select(self.table).order_by(self.table.id.desc())
        with self.session_maker() as session:
            last_instance = session.execute(query)
        return last_instance.scalars().first()
