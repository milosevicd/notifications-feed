from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields
from app.models.post import Post
from app.utils.db import db
import base64
    
class User(db.Model):
    __tablename__ = 'users'

    id = Column(String(32), primary_key=True)
    name = Column(String(255), nullable=True)
    avatar = Column(LargeBinary, nullable=True)

    def __init__(self, id, name, avatar = None):
        self.id = id
        self.name = name
        self.avatar = avatar

# Schema for User model, serializing and deserializing the avatar field as Base64
class Base64Field(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return base64.b64encode(value).decode()

    def _deserialize(self, value, attr, data, **kwargs):
        if value is None:
            return None
        return base64.b64decode(value)
    
class UserSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str(required=False)
    avatar = Base64Field(required=False)



