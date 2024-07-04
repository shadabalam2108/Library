from flask import jsonify,request,current_app,session
from functools import wraps
from app.md.models import Member
import jwt
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('token')

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = Member.query.filter_by(id=data['member_id']).first()
            if not current_user:
                return jsonify({'message': 'User not found!'}), 401
            if session['id']!=current_user.id:
                return jsonify({'message': 'Token is invalid!'}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token is invalid!'}), 401
        except Exception as e:
            return jsonify({'message': f'error: {e}'})

        return f(*args, **kwargs)
    return decorated