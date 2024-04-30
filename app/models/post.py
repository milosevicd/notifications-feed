from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields
from app.models.comment import Comment
from app.models.like import Like
from app.utils.db import db

class Post(db.Model):
    __tablename__ = 'posts'

    id = Column(String(32), primary_key=True)
    content = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=db.func.now())

    comments = relationship('Comment', lazy=True, back_populates='post')
    likes = relationship('Like', lazy=True, back_populates='post')

    def __init__(self, id, content):
        self.id = id
        self.content = content

# Schema for Post model, serializing and deserializing the Comments nested field as well
class PostWithCommentSchema(Schema):
    id = fields.Str(required=True)
    content = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    comments = fields.Nested('CommentSchema', many=True)

# Schema for Post model, serializing and deserializing the Likes nested field as well
class PostWithLikeSchema(Schema):
    id = fields.Str(required=True)
    content = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    likes = fields.Nested('LikeSchema', many=True)