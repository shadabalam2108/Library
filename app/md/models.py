from app import db
from werkzeug.security import check_password_hash


member_books = db.Table(
    'member_books',
    db.Column('user_id', db.Integer, db.ForeignKey('member.id'), primary_key=True),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True)
)

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    password = db.Column(db.String(700), nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    membership_status = db.Column(db.String(10), nullable=True) #for admin
    books = db.relationship("Book", secondary=member_books, backref='users', lazy=True)

    def verify_pass(self, password):
        return check_password_hash(self.password, password)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    publication_date = db.Column(db.String(30), nullable=True)
    genre = db.Column(db.String(50))
    count=db.Column(db.Integer,nullable=True)
    author_name = db.Column(db.String(30), db.ForeignKey('author.name'),nullable=True)

class Author(db.Model):
    name = db.Column(db.String(30),primary_key=True)
    bio = db.Column(db.Text)
    dob = db.Column(db.String(30), nullable=True)
    books = db.relationship('Book', backref='author', lazy=True)    