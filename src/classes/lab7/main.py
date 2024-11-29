"""
This is the main entry point for the Lab 7 application. It initializes the
DataController and runs the application.
"""

from src.classes.lab7.data_controller import DataController

def main():
    """
    Initializes the DataController and starts the data processing workflow.
    """
    controller = DataController()
    controller.run()

if __name__ == "__main__":
    main()
