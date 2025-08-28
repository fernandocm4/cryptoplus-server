from flask_restx import Resource, Namespace
from swagger.config import api
from swagger.user_model import user_payload, user_response

namespace_coin = Namespace("sdasd", path="/",description="operações de moeda")

@namespace_coin.route('/coins')
class CoinResource(Resource):
    @namespace_coin.doc('get_all_coins')
    def get(self):
        return {
            "status_code": 200,
            "msg": "Success"
        }
    
# @namespace_coin.route('/login')
# class LoginResource(Resource):
#     @namespace_coin.doc("login")
#     @namespace_coin.expect(user_payload)
#     @namespace_coin.marshal_with(user_response)
#     def post(self):
#         payload = {
#             "username": namespace_coin.payload["username"],
#             "password": namespace_coin.payload["password"]
#         }
#         return {"status_code":201, "msg":"Success", "data": payload}
