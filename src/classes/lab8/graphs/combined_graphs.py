import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class CombinedGraphs:
    """
    A class to generate combined graphs based on various columns in the dataset.

    The graphs include:
    - Histogram of 'MaxTemp'
    - Line graph of 'MaxTemp' and 'MinTemp' over time
    - Bar chart for 'RainToday' values
    - Scatter plot of 'MaxTemp' vs 'Rainfall'
    """

    def __init__(self, data):
        """
        Initializes the class with the provided data.

        :param data: DataFrame containing the dataset to visualize.
        """
        self.data = data

    def plot_combined_graphs(self):
        """
        Generates and displays a combination of graphs:
        - A histogram of 'MaxTemp'.
        - A line graph showing 'MaxTemp' and 'MinTemp' over time.
        - A bar graph of 'RainToday' values (Yes vs No).
        - A scatter plot of 'MaxTemp' vs 'Rainfall'.
        """
        fig, axs = plt.subplots(2, 2, figsize=(12, 10))

        # Plot histogram if 'MaxTemp' column exists in the data
        if 'MaxTemp' in self.data.columns:
            axs[0, 0].hist(self.data['MaxTemp'], bins=30, color='green', edgecolor='black', alpha=0.7)
            axs[0, 0].set_title('Distribution of Max Temperature')
            axs[0, 0].set_xlabel('Max Temperature (°C)')
            axs[0, 0].set_ylabel('Frequency')
            axs[0, 0].grid(True)

        # Plot line graph if 'Date', 'MaxTemp', and 'MinTemp' columns exist in the data
        if 'Date' in self.data.columns and 'MaxTemp' in self.data.columns and 'MinTemp' in self.data.columns:
            self.data['Date'] = pd.to_datetime(self.data['Date'])
            axs[0, 1].plot(self.data['Date'], self.data['MaxTemp'], label='Max Temperature', color='red')
            axs[0, 1].plot(self.data['Date'], self.data['MinTemp'], label='Min Temperature', color='blue')
            axs[0, 1].set_title('Max and Min Temperature Over Time')
            axs[0, 1].set_xlabel('Date')
            axs[0, 1].set_ylabel('Temperature (°C)')
            axs[0, 1].legend()
            axs[0, 1].grid(True)

        # Plot bar graph if 'RainToday' column exists in the data
        if 'RainToday' in self.data.columns:
            rain_today_counts = self.data['RainToday'].value_counts()
            axs[1, 0].bar(rain_today_counts.index, rain_today_counts.values, color=['skyblue', 'orange'])
            axs[1, 0].set_title('Rain Today (Yes vs No)')
            axs[1, 0].set_xlabel('Rain Today')
            axs[1, 0].set_ylabel('Number of Days')

        # Plot scatter graph if 'MaxTemp' and 'Rainfall' columns exist in the data
        if 'MaxTemp' in self.data.columns and 'Rainfall' in self.data.columns:
            sns.scatterplot(data=self.data, x='MaxTemp', y='Rainfall', hue='RainToday', palette='coolwarm',
                            ax=axs[1, 1])
            axs[1, 1].set_title('Max Temperature vs Rainfall')
            axs[1, 1].set_xlabel('Max Temperature (°C)')
            axs[1, 1].set_ylabel('Rainfall (mm)')

        # Adjust the layout for better spacing
        plt.tight_layout()
        plt.show()
