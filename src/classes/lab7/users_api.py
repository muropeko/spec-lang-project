from lib import ApiService

class UsersAPI:
    def get_data(self):
        client = ApiService()
        return client.get_data('users')
