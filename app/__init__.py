from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()
def create_app():
    
    app=Flask(__name__)
    app.config['SECRET_KEY']="cpr490cd"
    app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:0000@localhost:5432/lms"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    db.init_app(app)
    from .auth.controllers.login import login
    app.register_blueprint(login,url_prefix='/api/auth/')
    from .auth.controllers.logout import logout
    app.register_blueprint(logout,url_prefix='/api/auth/')
    from .auth.controllers.register import register
    app.register_blueprint(register,url_prefix='/api/auth/')

    from .md.crud import library
    app.register_blueprint(library,url_prefix='/library/')
    

    return app  


    