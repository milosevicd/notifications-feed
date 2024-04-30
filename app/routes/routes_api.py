from flask import Blueprint, jsonify
from app.models.like import Like
from app.models.post import Post, PostWithLikeSchema, PostWithCommentSchema
from app.models.comment import Comment, CommentSchema
from app.models.user import User, UserSchema
from app.utils.db import db
from sqlalchemy.orm import joinedload

routes_api = Blueprint('routes_api', __name__)

# endpoint for getting notifications aggregated by posts with likes and comments
@routes_api.route('/notifications/aggregate', methods=['GET'])
def get_aggregate_notifications():
    """
    Get notifications aggregated by posts
    Each notification aggregation contains either a list of comments or a list of likes for a post. 
    Each comment or like contains the user that created it. If a user has an avatar, its returned in the response as base64 encoded string.
    ---
    responses:
        200:
            description: A JSON object with the notifications aggregated by posts
    """
    
    # retrieve posts, joined with comments and users that commented
    posts_and_comments = Post.query.options(joinedload(Post.comments).joinedload(Comment.user)).all()

    # retrieve posts, joined with likes and users that liked
    posts_and_likes = Post.query.options(joinedload(Post.likes).joinedload(Like.user)).all()

    # return a joined list of posts with comments and posts with likes
    return PostWithCommentSchema(many=True).dump(posts_and_comments) + PostWithLikeSchema(many=True).dump(posts_and_likes)

