from src.classes.lab7.api_manager import APIManager
from src.ui.lab7.ui import UserInterface

from lib import DataSaver, HistoryLogger

class DataController:
    """Controller that manages user interaction, data retrieval, and saving."""
    def __init__(self):
        self.ui = UserInterface()
        self.api_manager = APIManager()
        self.history_logger = HistoryLogger()

    def run(self):
        """Starts the application and processes user choices."""
        try:
            while True:
                user_choice = self.ui.get_user_choice()
                if user_choice is None:
                    break

                client = self.api_manager.create_client(user_choice)
                data = client.get_data()

                if data is not None:
                    self.ui.display_data(data)
                else:
                    print("Failed to retrieve data.")

                if self.ui.ask_save_data():
                    format_choice, filename = self.ui.get_save_options()
                    DataSaver.save_data(data, format_choice, filename)

                self.history_logger.log(user_choice)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
