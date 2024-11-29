"""
This module manages the creation of API clients for different data types
(posts, users, and comments) and provides a method to format data for output.
"""

from src.classes.lab7.comments_api import CommentsAPI
from src.classes.lab7.posts_api import PostsAPI
from src.classes.lab7.users_api import UsersAPI

class APIManager:
    """Manages the creation of API clients based on the data type."""
    client_classes = {
        'posts': PostsAPI,
        'users': UsersAPI,
        'comments': CommentsAPI
    }

    @classmethod
    def create_client(cls, data_type):
        """Creates and returns an API client for the specified data type."""
        try:
            return cls.client_classes[data_type]()
        except KeyError as exc:
            raise ValueError("! unknown type of data") from exc

    @staticmethod
    def format_data(data):
        """Formats data for output."""
        return "\n".join(map(str, data)) if isinstance(data, list) else str(data)
