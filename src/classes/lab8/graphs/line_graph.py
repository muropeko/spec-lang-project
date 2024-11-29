import matplotlib.pyplot as plt
from src.classes.lab8.graph_template import GraphTemplate
import pandas as pd


class LineGraph(GraphTemplate):
    """
    A class to create a line graph for visualizing the 'MaxTemp' and 'MinTemp' columns over time.

    Inherits from GraphTemplate and overrides methods to setup the data and plot the line graph.
    """

    def setup_data(self):
        """
        Prepares the data for plotting. Converts the 'Date' column to datetime format and selects
        the 'MaxTemp' and 'MinTemp' columns along with 'Date'.

        :return: None
        """
        if 'Date' in self.data.columns:
            self.data['Date'] = pd.to_datetime(self.data['Date'])
            self.data_to_plot = self.data[['Date', 'MaxTemp', 'MinTemp']]

    def plot_graph(self):
        """
        Plots the line graph showing 'MaxTemp' and 'MinTemp' against 'Date'.

        - Plots the 'MaxTemp' and 'MinTemp' columns as separate lines.
        - Adds a title and labels for the axes.
        - Displays the legend to identify each line.
        - Adds a grid for readability.
        - Rotates the x-axis labels for better visibility.
        - Displays the plot.
        """
        if hasattr(self, 'data_to_plot'):
            plt.figure(figsize=(10, 6))
            plt.plot(self.data_to_plot['Date'], self.data_to_plot['MaxTemp'], label='Max Temperature', color='red')
            plt.plot(self.data_to_plot['Date'], self.data_to_plot['MinTemp'], label='Min Temperature', color='yellow')
            plt.title('Max and Min Temperature Over Time')
            plt.xlabel('Date')
            plt.ylabel('Temperature (°C)')
            plt.legend()
            plt.grid(True)
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
