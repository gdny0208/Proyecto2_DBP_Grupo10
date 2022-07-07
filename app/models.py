from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_migrate import Migrate
from flask_login import UserMixin
import json

database_name = "yape3"
database_path = "postgresql+psycopg2://{}@{}/{}".format('postgres:2000', 'localhost:5432', database_name)

db=SQLAlchemy()
migrate=Migrate()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SECRET_KEY"] = "secret"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    migrate.init_app(app, db)
    db.create_all()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True,)
    email = db.Column(db.String(150), unique=True,  nullable=False)
    username = db.Column(db.String(150), unique=True,  nullable=False)
    password = db.Column(db.String(150),  nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now(), nullable=False)
    posts = db.relationship('Post', backref='user', passive_deletes=True)
    comments = db.relationship('Comment', backref='user', passive_deletes=True)
    likes = db.relationship('Like', backref='user', passive_deletes=True)

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()
    
    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
    
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

    def format(self):
        return {
            'id': self.id,
            'email': self.email,
            'username': self.username,
            'date_created': self.date_created
        }
    
    def __repr__(self):
        return f'User: id={self.id}  username={self.username}'
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now(),  nullable=False)
    author = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete="CASCADE"), nullable=False)
    comments = db.relationship('Comment', backref='post', passive_deletes=True)
    likes = db.relationship('Like', backref='post', passive_deletes=True)

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()
    
    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
    
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
    
    def __init__(self, text, author):
        self.text = text
        self.author = author

    def format(self):
        return {
            'id': self.id,
            'text': self.text,
            'date_created': self.date_created,
            'author': self.author
        }
    
    def __repr__(self):
        return f'Post: id={self.id}  text={self.text}'

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now(),  nullable=False)
    author = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey(
        'post.id', ondelete="CASCADE"), nullable=False)
    
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()
    
    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
    
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def __init__(self, text, author, post_id):
        self.text = text
        self.author = author
        self.post_id = post_id

    def format(self):
        return {
            'id': self.id,
            'text': self.text,
            'date_created': self.date_created,
            'author': self.author,
            'post_id': self.post_id
        }
    
    def __repr__(self):
        return f'Comment: id={self.id}  text={self.text}'
    
class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    author = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey(
        'post.id', ondelete="CASCADE"), nullable=False)

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()
    
    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
    
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def __init__(self, author, post_id):
        self.author = author
        self.post_id = post_id
    
    def format(self):
        return {
            'id': self.id,
            'date_created': self.date_created,
            'author': self.author,
            'post_id': self.post_id
        }
    
    def __repr__(self):
        return f'Like: id={self.id}  author={self.author}'




