from peewee import CharField, Model, UUIDField
from uuid import uuid4
from database.config import db


class User(Model):
    id = UUIDField(null=False, primary_key=True, default=uuid4)
    name = CharField()
    username = CharField()
    password = CharField()

    class Meta:
        database=db
        db_table = 'User'