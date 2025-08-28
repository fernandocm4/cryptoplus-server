from peewee import PostgresqlDatabase
from dotenv import load_dotenv
import os
load_dotenv()




db = PostgresqlDatabase(
    os.getenv('DATABASE_NAME'),
    host=os.getenv('DATABASE_URL'),
    port=os.getenv('DATABASE_PORT'),
    user=os.getenv('DATABASE_USER'),
    password=os.getenv('DATABASE_PWD')
)