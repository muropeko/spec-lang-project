import os
import json
import csv
from src.const.path_constants import FOLDER_PATH_RESULT_LAB7

class DataSaver:
    """Handles the saving of data in different formats."""
    @staticmethod
    def save_data(data, format_choice, filename):
        """Saves the data to a specified format and filename."""
        results_dir = FOLDER_PATH_RESULT_LAB7
        os.makedirs(results_dir, exist_ok=True)

        file_path = os.path.join(results_dir, filename)

        if format_choice == 'json':
            DataSaver.save_json(data, file_path)
        elif format_choice == 'csv':
            DataSaver.save_csv(data, file_path)
        elif format_choice == 'txt':
            DataSaver.save_txt(data, file_path)
        else:
            print("Unsupported format type.")

    @staticmethod
    def save_json(data, file_path):
        """Saves data in JSON format."""
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data saved in JSON format to {file_path}")

    @staticmethod
    def save_csv(data, file_path):
        """Saves data in CSV format."""
        with open(file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            if data:
                writer.writerow(data[0].keys())
                for item in data:
                    writer.writerow(item.values())
        print(f"Data saved in CSV format to {file_path}")

    @staticmethod
    def save_txt(data, file_path):
        """Saves data in plain text format."""
        with open(file_path, 'w') as txt_file:
            for item in data:
                txt_file.write(str(item) + "\n")
        print(f"Data saved in plain text format to {file_path}")
