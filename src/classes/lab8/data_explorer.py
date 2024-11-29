class DataExplorer:
    """
    A class for exploring and summarizing data.

    This class provides functionality to explore numeric data in a dataset, specifically
    calculating and displaying the minimum and maximum values for numeric columns.
    """

    def __init__(self, data):
        """
        Initializes the DataExplorer with the provided dataset.

        Parameters:
            data (pd.DataFrame): The dataset to be explored.
        """
        self.data = data

    def explore_data(self):
        """
        Explores the dataset by calculating the minimum and maximum values for numeric columns.

        If the dataset is valid (non-None), this method will print the minimum and maximum values
        for each numeric column in the dataset.
        """
        if self.data is not None:
            numeric_data = self.data.select_dtypes(include=['number'])
            print("Minimum values by numeric columns:")
            print(numeric_data.min())
            print("\nMaximum values by numeric columns:")
            print(numeric_data.max())

    def configure(self):
        """
        A placeholder method for future configuration (currently not implemented).

        This method can be extended in the future if there is a need to configure the
        `DataExplorer` class in any specific way.
        """
        pass
