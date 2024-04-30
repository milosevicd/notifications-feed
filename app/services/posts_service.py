from app.models.like import Like
from app.models.post import Post, PostWithLikeSchema, PostWithCommentSchema
from app.models.comment import Comment
from sqlalchemy.orm import joinedload

# Retrieve all posts with comments and likes
def get_aggregate_notifications():
    
    # retrieve posts, joined with comments and users that commented
    posts_and_comments = Post.query.options(joinedload(Post.comments).joinedload(Comment.user)).all()

    # retrieve posts, joined with likes and users that liked
    posts_and_likes = Post.query.options(joinedload(Post.likes).joinedload(Like.user)).all()

    # return a joined list of posts with comments and posts with likes
    return PostWithCommentSchema(many=True).dump(posts_and_comments) + PostWithLikeSchema(many=True).dump(posts_and_likes)

