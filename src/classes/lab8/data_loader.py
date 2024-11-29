import pandas as pd


class DataLoader:
    """
    A class responsible for loading and preprocessing data from a CSV file.

    This class reads data from a given file path, preprocesses it by handling missing values,
    converting data types, and extracting date-related features.
    """

    def __init__(self, file_path):
        """
        Initializes the DataLoader with the provided file path.

        Parameters:
            file_path (str): The path to the CSV file to be loaded.
        """
        self.file_path = file_path
        self.data = None

    def load_data(self):
        """
        Loads data from the CSV file specified by the file path.

        This method reads the file into a pandas DataFrame and then calls the preprocessing
        method to clean and format the data. It prints a success or error message.

        Returns:
            pandas.DataFrame: The loaded and preprocessed data.
        """
        try:
            self.data = pd.read_csv(self.file_path)
            self.preprocess_data()
            print("Data successfully loaded.")
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
        return self.data

    def preprocess_data(self):
        """
        Preprocesses the loaded data by handling missing values, converting data types,
        and extracting date-related features.

        - Converts the 'Date' column to datetime format.
        - Fills missing numeric values with the mean of the column.
        - Fills missing categorical values with the mode (most frequent value).
        - Drops duplicate rows.
        - Extracts 'Year', 'Month', and 'Day' from the 'Date' column, if present.
        """
        if 'Date' in self.data.columns:
            self.data['Date'] = pd.to_datetime(self.data['Date'], errors='coerce')

        for column in self.data.select_dtypes(include=['float64', 'int64']).columns:
            self.data[column].fillna(self.data[column].mean(), inplace=True)

        for column in self.data.select_dtypes(include=['object']).columns:
            self.data[column].fillna(self.data[column].mode()[0], inplace=True)

        self.data.drop_duplicates(inplace=True)

        if 'Date' in self.data.columns:
            self.data['Year'] = self.data['Date'].dt.year
            self.data['Month'] = self.data['Date'].dt.month
            self.data['Day'] = self.data['Date'].dt.day
