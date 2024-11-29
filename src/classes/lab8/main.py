"""
This module loads, processes, and visualizes weather data.
It uses the DataHandler class to load the data, explore it,
and create different types of visualizations such as histograms,
line charts, and bar charts.
"""

from src.classes.lab8.data_handler import DataHandler
from src.const.path_constants import FOLDER_PATH_DATA


def main():
    """
    The main function to initialize the DataHandler, load the data,
    explore it, and generate visualizations.
    """
    file_path = FOLDER_PATH_DATA

    data_handler = DataHandler(file_path)
    data_handler.load_data()
    data_handler.create_all_graphs()


if __name__ == "__main__":
    main()
