from peewee import CharField, Model, UUIDField, DecimalField, DateTimeField
import datetime
from uuid import uuid4
from database.config import db


class Coin(Model):
    id = UUIDField(null=False, primary_key=True, default=uuid4)
    name = CharField()
    symbol = CharField()
    image = CharField()
    current_price = DecimalField(decimal_places=4)
    save_data = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database=db
        db_table = 'Coin'