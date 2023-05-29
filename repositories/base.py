import typing
from dataclasses import dataclass, field

from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker


@dataclass
class BaseRepo:
    table: typing.Any = field(init=False)
    engine: Engine
    session_maker: sessionmaker
