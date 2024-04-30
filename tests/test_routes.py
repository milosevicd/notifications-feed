import pytest

from app.models.comment import Comment
from app.models.like import Like
from app.models.post import Post
from app.utils.db import db
from app.utils.app_factory import create_app
from app.utils.config import TestingConfig

@pytest.fixture
def app():
    app = create_app(TestingConfig)
    yield app

@pytest.fixture
def client(app):
    return app.test_client()  # Use the same app context as created in the app fixture


def test_empty_db(client):

    response = client.get('/api/notifications/aggregate')

    assert response.status_code == 200
    assert response.json == []


def test_single_post(app, client):

    with app.app_context():
        post = Post(id="post_id_123", content="content of post")
        db.session.add(post)
        db.session.commit()

    response = client.get('/api/notifications/aggregate')

    assert response.status_code == 200
    assert len(response.json) == 2
    # Check the first notification (about comments)
    assert response.json[0]['id'] == "post_id_123"
    assert response.json[0]['content'] == "content of post"
    assert response.json[0]['comments'] == []
    assert response.json[0]['created_at'] is not None

    # Check the second notification (about likes)
    assert response.json[1]['id'] == "post_id_123"
    assert response.json[1]['content'] == "content of post"
    assert response.json[1]['likes'] == []
    assert response.json[1]['created_at'] is not None


def test_single_post_with_comment(app, client):
    
        with app.app_context():
            post = Post(id="post_id_123", content="content of post")
            comment = Comment(id="comment_id_123", post_id="post_id_123", content="comment content", user_id="user_id_123")
            db.session.add(post)
            db.session.add(comment)
            db.session.commit()
    
        response = client.get('/api/notifications/aggregate')
    
        assert response.status_code == 200
        assert len(response.json) == 2
        # Check the first notification (about comments)
        assert response.json[0]['id'] == "post_id_123"
        assert response.json[0]['content'] == "content of post"
        assert len(response.json[0]['comments']) == 1
        assert response.json[0]['comments'][0]['id'] == "comment_id_123"
        assert response.json[0]['comments'][0]['content'] == "comment content"
        assert response.json[0]['comments'][0]['user_id'] == "user_id_123"
        assert response.json[0]['created_at'] is not None
    
        # Check the second notification (about likes)
        assert response.json[1]['id'] == "post_id_123"
        assert response.json[1]['content'] == "content of post"
        assert response.json[1]['likes'] == []
        assert response.json[1]['created_at'] is not None


def test_single_post_with_like(app, client):
    
        with app.app_context():
            post = Post(id="post_id_123", content="content of post")
            like = Like(id="like_id_123", post_id="post_id_123", user_id="user_id_123")
            db.session.add(post)
            db.session.add(like)
            db.session.commit()
    
        response = client.get('/api/notifications/aggregate')
    
        assert response.status_code == 200
        assert len(response.json) == 2
        # Check the first notification (about comments)
        assert response.json[0]['id'] == "post_id_123"
        assert response.json[0]['content'] == "content of post"
        assert response.json[0]['comments'] == []
        assert response.json[0]['created_at'] is not None
    
        # Check the second notification (about likes)
        assert response.json[1]['id'] == "post_id_123"
        assert response.json[1]['content'] == "content of post"
        assert len(response.json[1]['likes']) == 1
        assert response.json[1]['likes'][0]['id'] == "like_id_123"
        assert response.json[1]['likes'][0]['user_id'] == "user_id_123"
        assert response.json[1]['created_at'] is not None


def test_single_post_with_comment_and_like(app, client):
        
            with app.app_context():
                post = Post(id="post_id_123", content="content of post")
                comment = Comment(id="comment_id_123", post_id="post_id_123", content="comment content", user_id="user_id_123")
                like = Like(id="like_id_123", post_id="post_id_123", user_id="user_id_123")
                db.session.add(post)
                db.session.add(comment)
                db.session.add(like)
                db.session.commit()
        
            response = client.get('/api/notifications/aggregate')
        
            assert response.status_code == 200
            assert len(response.json) == 2
            # Check the first notification (about comments)
            assert response.json[0]['id'] == "post_id_123"
            assert response.json[0]['content'] == "content of post"
            assert len(response.json[0]['comments']) == 1
            assert response.json[0]['comments'][0]['id'] == "comment_id_123"
            assert response.json[0]['comments'][0]['content'] == "comment content"
            assert response.json[0]['comments'][0]['user_id'] == "user_id_123"
            assert response.json[0]['created_at'] is not None
        
            # Check the second notification (about likes)
            assert response.json[1]['id'] == "post_id_123"
            assert response.json[1]['content'] == "content of post"
            assert len(response.json[1]['likes']) == 1
            assert response.json[1]['likes'][0]['id'] == "like_id_123"
            assert response.json[1]['likes'][0]['user_id'] == "user_id_123"
            assert response.json[1]['created_at'] is not None


def test_multiple_posts(app, client):
        
            with app.app_context():
                post1 = Post(id="post_id_123", content="content of post 1")
                post2 = Post(id="post_id_456", content="content of post 2")
                db.session.add(post1)
                db.session.add(post2)
                db.session.commit()
        
            response = client.get('/api/notifications/aggregate')
        
            assert response.status_code == 200
            assert len(response.json) == 4
            
            # Check the first notification (about comments)
            assert response.json[0]['id'] == "post_id_123"
            assert response.json[0]['content'] == "content of post 1"
            assert response.json[0]['comments'] == []
            assert response.json[0]['created_at'] is not None
        
            # Check the second notification (about comments)
            assert response.json[1]['id'] == "post_id_456"
            assert response.json[1]['content'] == "content of post 2"
            assert response.json[1]['comments'] == []
            assert response.json[1]['created_at'] is not None
        
            # Check the third notification (about likes)
            assert response.json[2]['id'] == "post_id_123"
            assert response.json[2]['content'] == "content of post 1"
            assert response.json[2]['likes'] == []
            assert response.json[2]['created_at'] is not None
        
            # Check the fourth notification (about likes)
            assert response.json[3]['id'] == "post_id_456"
            assert response.json[3]['content'] == "content of post 2"
            assert response.json[3]['likes'] == []
            assert response.json[3]['created_at'] is not None


def test_multiple_posts_with_comments_and_likes(app, client):
        
            with app.app_context():
                post1 = Post(id="post_id_123", content="content of post 1")
                post2 = Post(id="post_id_456", content="content of post 2")
                comment1 = Comment(id="comment_id_123", post_id="post_id_123", content="comment content 1", user_id="user_id_123")
                comment2 = Comment(id="comment_id_456", post_id="post_id_123", content="comment content 2", user_id="user_id_456")
                comment3 = Comment(id="comment_id_789", post_id="post_id_456", content="comment content 3", user_id="user_id_789")
                like1 = Like(id="like_id_123", post_id="post_id_123", user_id="user_id_123")
                like2 = Like(id="like_id_456", post_id="post_id_123", user_id="user_id_456")
                like3 = Like(id="like_id_789", post_id="post_id_456", user_id="user_id_789")
                db.session.add(post1)
                db.session.add(post2)
                db.session.add(comment1)
                db.session.add(comment2)
                db.session.add(comment3)
                db.session.add(like1)
                db.session.add(like2)
                db.session.add(like3)
                db.session.commit()
        
            response = client.get('/api/notifications/aggregate')
        
            assert response.status_code == 200
            assert len(response.json) == 4
            
            # Check the first notification (about comments)
            assert response.json[0]['id'] == "post_id_123"
            assert response.json[0]['content'] == "content of post 1"
            assert len(response.json[0]['comments']) == 2
            assert response.json[0]['comments'][0]['id'] == "comment_id_123"
            assert response.json[0]['comments'][0]['content'] == "comment content 1"
            assert response.json[0]['comments'][0]['user_id'] == "user_id_123"
            assert response.json[0]['comments'][1]['id'] == "comment_id_456"
            assert response.json[0]['comments'][1]['content'] == "comment content 2"
            assert response.json[0]['comments'][1]['user_id'] == "user_id_456"
            assert response.json[0]['created_at'] is not None

            # Check the second notification (about comments)
            assert response.json[1]['id'] == "post_id_456"
            assert response.json[1]['content'] == "content of post 2"
            assert len(response.json[1]['comments']) == 1
            assert response.json[1]['comments'][0]['id'] == "comment_id_789"
            assert response.json[1]['comments'][0]['content'] == "comment content 3"
            assert response.json[1]['comments'][0]['user_id'] == "user_id_789"
            assert response.json[1]['created_at'] is not None

            # Check the third notification (about likes)
            assert response.json[2]['id'] == "post_id_123"
            assert response.json[2]['content'] == "content of post 1"
            assert len(response.json[2]['likes']) == 2
            assert response.json[2]['likes'][0]['id'] == "like_id_123"
            assert response.json[2]['likes'][0]['user_id'] == "user_id_123"
            assert response.json[2]['likes'][1]['id'] == "like_id_456"
            assert response.json[2]['likes'][1]['user_id'] == "user_id_456"
            assert response.json[2]['created_at'] is not None

            # Check the fourth notification (about likes)
            assert response.json[3]['id'] == "post_id_456"
            assert response.json[3]['content'] == "content of post 2"
            assert len(response.json[3]['likes']) == 1
            assert response.json[3]['likes'][0]['id'] == "like_id_789"
            assert response.json[3]['likes'][0]['user_id'] == "user_id_789"
            assert response.json[3]['created_at'] is not None




