from flask import session,jsonify
from app.md.models import Member
from functools import wraps


def admin_only(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        member=Member.query.filter_by(id=session.get('id')).first()
        if member.membership_status == "admin":
            return f(*args,**kwargs)
        else:
            return jsonify({'message':'unauthorized access'}),403   
    return decorated    