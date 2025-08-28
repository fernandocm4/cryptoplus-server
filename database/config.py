from peewee import PostgresqlDatabase
from dotenv import load_dotenv
import os
from urllib.parse import urlparse
load_dotenv()


database_url = os.getenv('DATABASE_URL')
url = urlparse(database_url)

db = PostgresqlDatabase(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)