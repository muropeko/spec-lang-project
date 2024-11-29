from lib import ApiService

class PostsAPI:
    def get_data(self):
        client = ApiService()
        return client.get_data('posts')
