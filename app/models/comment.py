from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields
from app.utils.db import db

class Comment(db.Model):
    __tablename__ = 'comments'

    id = Column(String(32), primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    content = Column(String)
    created_at = Column(DateTime, server_default=db.func.now())
    
    post = relationship('Post', back_populates='comments')
    user = relationship('User')

    def __init__(self, id, post_id, user_id, content):
        self.id = id
        self.post_id = post_id
        self.user_id = user_id
        self.content = content

class CommentSchema(Schema):
    id = fields.Str(required=True)
    post_id = fields.Str()
    user_id = fields.Str()
    content = fields.Str()
    created_at = fields.DateTime(dump_only=True)
    user = fields.Nested('UserSchema')
