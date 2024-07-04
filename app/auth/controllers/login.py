from flask import jsonify,request,Blueprint,current_app,session
import jwt
from app.md.serde import Members_schema
from marshmallow import ValidationError
from app.md.models import Member
from datetime import datetime, timedelta,timezone

login=Blueprint("login",__name__)


@login.route('/login', methods=['POST'])
def post():
    credentials = request.get_json()
    user = Member.query.filter_by(name=credentials["name"]).first()

    try:
        va = Members_schema().load(credentials)
    except ValidationError as e:
        return jsonify({'message':'Validation Error', 'errors':e}), 422
    
    if not user or not user.verify_pass(credentials["password"]):
        return jsonify({'message': 'Invalid username or password'}), 401

    session['id'] = user.id
    print("Session after login:", session)  # Debug print
    print("User's ID:", user.id)

    token = jwt.encode({
        'member_id': user.id,
        'exp': datetime.now(timezone.utc) + timedelta(minutes=10)
    }, current_app.config['SECRET_KEY'], algorithm="HS256")

    response = jsonify({'message':'login successfull'})
    response.set_cookie("token", token, httponly=True) 
    return response