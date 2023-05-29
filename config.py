class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 4}


QUESTIONS_API = f'https://jservice.io/api/random?count='
DATABASE_URI = 'postgresql://postgres:12345678@db:5432/Flask'
