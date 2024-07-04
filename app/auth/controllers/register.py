from flask import jsonify,request,Blueprint
from app import db
from app. md.serde import Members_schema
from marshmallow import ValidationError
from app.md.models import Member
from werkzeug.security import generate_password_hash

register=Blueprint("register",__name__)

@register.route('/register', methods=['POST'])
def post():
    data = request.get_json()

    try:
        va = Members_schema().load(data)
    except ValidationError as e:
        return jsonify({'message':'Validation Error', 'errors':e}), 422
    
    if Member.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already exists'}), 400
    
    if len(data["name"]) < 2:
        return jsonify({'message': 'First name must be greater than 1 character.'}), 400
    
    if len(data["password"]) < 7:
        return jsonify({'message': 'Password must be at least 7 characters.'}), 400
    hashed_password = generate_password_hash(data["password"])
    
    user = Member(
        name=data['name'],
        password=hashed_password,
        email=data['email'],
        membership_status=data.get('membership_status'),
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'})