from datetime import datetime

class HistoryLogger:
    """Logs the history of user choices."""
    @staticmethod
    def log(user_choice):
        """Logs the user's choice."""
        with open('user_history.log', 'a') as log_file:
            log_file.write(f"{datetime.now()} - {user_choice}\n")
