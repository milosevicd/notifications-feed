import logging
import os
import json
from app.models.user import User
from app.models.post import Post
from app.models.comment import Comment
from app.models.like import Like
from app.utils.db import db
import secrets

# read avatar from file
def read_avatar(avatar):
    if not avatar:
        return None
    avatar_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'db_init_data/avatars', avatar)
    if os.path.exists(avatar_path):
        with open(avatar_path, 'rb') as file:
            return file.read()
    return None

# Add or update user (assume that the first item in the JSON data is the correct user, and ignore any subsequent user data)
def get_or_create_user(user_data):
    user = User.query.filter_by(id=user_data['id']).first()
    
    if not user:
        logging.debug(f'Creating user {user_data["id"]}')
        
        # if the avatar is specified for the user, load it from avatars folder
        avatar_data = read_avatar(user_data.get('avatar', None))
        
        user = User(id=user_data['id'], name=user_data.get('name', ''), avatar=avatar_data)

        db.session.add(user)

    return user

# Add or update post (assume that the first item in the JSON data is the correct post, and ignore any subsequent post data)
def get_or_create_post(post_data):
    post = Post.query.filter_by(id=post_data['id']).first()
    if not post:
        logging.debug(f'Creating post {post_data["id"]}')
        post = Post(id=post_data['id'], content=post_data['title'])
        db.session.add(post)
    return post

def process_json_to_db():
    # Construct the full path to the JSON file
    logging.info('Loading JSON data to database')
    dir_path = os.path.dirname(os.path.realpath(__file__))
    json_path = os.path.join(dir_path, 'db_init_data/notifications-feed.json')

    # Load JSON data
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    logging.debug(f'Processing total of {len(data)} likes and comments')
    # Process likes and comments in the JSON data; 
    # first appearance of a user will create it; similarly, first appearance of a post will create it
    for item in data:
        user = get_or_create_user(item['user'])
        post = get_or_create_post(item['post'])
        if item['type'] == 'Comment':
            comment = Comment(id=item['comment']['id'], content=item['comment']['commentText'], post_id=post.id, user_id=user.id)
            db.session.add(comment)
        elif item['type'] == 'Like':
            like = Like(id= secrets.token_hex(16), post_id=post.id, user_id=user.id)
            db.session.add(like)

    db.session.commit()

    logging.info('Loading JSON data to database completed')