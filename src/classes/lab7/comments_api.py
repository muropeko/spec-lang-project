from lib import ApiService

class CommentsAPI:
    """API client for fetching comment data."""
    def get_data(self):
        """Fetches comments data from the API."""
        client = ApiService()
        return client.get_data('comments')
