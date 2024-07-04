from flask import jsonify,request,Blueprint,session
from app.auth.decorators.user_auth import token_required



logout=Blueprint("logout",__name__)

@logout.route("/logout", methods=['GET'])
@token_required
def post():
    # token = request.cookies.get("token")
    # if token:
    session.pop('id')
    response = jsonify({'message': 'Logout successfull'})
    response.delete_cookie('token')
    return response