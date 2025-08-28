from flask_restx import fields
from swagger.config import api

user_payload = api.model(
    "Payload",
    {
        "username": fields.String,
        "password": fields.String
    },
)

user_response = api.model(
    "Response",
    {
        "status_code":fields.Integer,
        "msg": fields.String,
        "data": fields.Nested(user_payload),
    },
)