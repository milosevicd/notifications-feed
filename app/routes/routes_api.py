from flask import Blueprint
from app.services import posts_service
from app.utils.db import db

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

    return posts_service.get_aggregate_notifications()
    