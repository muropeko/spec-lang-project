from src.classes.lab8.graph_template import GraphTemplate
import matplotlib.pyplot as plt


class HistogramGraph(GraphTemplate):
    """
    A class to create a histogram of the 'MaxTemp' column in the dataset.

    Inherits from GraphTemplate and overrides methods to setup the data and plot the histogram.
    """

    def setup_data(self):
        """
        Prepares the data to be plotted. In this case, the 'MaxTemp' column is selected from the data.

        :return: None
        """
        self.data_to_plot = self.data['MaxTemp']

    def plot_graph(self):
        """
        Plots the histogram of the 'MaxTemp' data.

        - Sets the figure size.
        - Defines the number of bins.
        - Sets the color of the bars.
        - Adds grid lines for better readability.
        - Displays the plot.
        """
        plt.figure(figsize=(8, 6))
        self.data_to_plot.plot(kind='hist', bins=30, color='green', edgecolor='black', alpha=0.7)
        plt.title('Temperature Distribution')
        plt.xlabel('Max Temperature (°C)')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()
