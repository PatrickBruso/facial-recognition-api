import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    PROJECT_DIR = os.path.abspath(os.path.dirname(BASE_DIR))

    DB_URL = os.getenv("DB_HOST")  # TODO: get db url from env
    SQLALCHEMY_DATABASE_URI = f"postgresql://root:root@localhost:5432/facial-recognition"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MIGRATION_DIR = BASE_DIR + "/migrations"

    INIT_TASK_WORKERS = 2
