import logging


class BaseConfig:
    ENVIRONMENT: str
    LOGGING_LEVEL = logging.INFO

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1/catalog"
    SQLALCHEMY_ENGINE_OPTIONS = {
        "max_overflow": 0,
        "pool_size": 0,
        "echo": False,
    }
