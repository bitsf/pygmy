from pygmy.model import *
from pygmy.config import config
from pygmy.database.sqlite import SqliteDatabase
from pygmy.database.base import Model


class DatabaseFactory:

    @staticmethod
    def create():
        database = SqliteDatabase()
        database.initialize(config.debug)
        # Create all tables, if not already exists.
        Model.metadata.create_all(database.engine)
        return database
