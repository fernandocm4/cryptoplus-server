from routes.home import home_route
from routes.coins import coins_route
from auth.authentication import auth_route
from swagger.config import api
from swagger.coins_doc import namespace_coin
from database.config import db
from database.models.coin import Coin
from database.models.user import User


def config_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(coins_route)
    app.register_blueprint(auth_route)

def config(app):
    config_routes(app)
    api.init_app(app)
    api.add_namespace(namespace_coin)
    configure_db()

def configure_db():
    db.connect()
    db.create_tables([Coin])
    db.create_tables([User])