import matplotlib.pyplot as plt
from src.classes.lab8.graph_template import GraphTemplate


class PieGraph(GraphTemplate):
    """
    A class to create a pie chart visualizing the proportion of 'RainToday' values (Yes vs No).

    Inherits from GraphTemplate and overrides methods to setup the data and plot the pie chart.
    """

    def setup_data(self):
        """
        Prepares the data for plotting by counting the occurrences of 'RainToday' values
        (e.g., 'Yes' or 'No').

        :return: None
        """
        self.data_to_plot = self.data['RainToday'].value_counts()

    def plot_graph(self):
        """
        Plots the pie chart showing the proportion of 'RainToday' values.

        - Creates a pie chart where slices represent 'Yes' and 'No' values for 'RainToday'.
        - Displays the percentage for each slice.
        - Customizes the colors for the slices.
        - Adds a title to the chart and removes the y-label.
        - Displays the plot.
        """
        plt.figure(figsize=(7, 7))
        self.data_to_plot.plot(kind='pie', autopct='%1.1f%%', colors=['lightcoral', 'lightgreen'])
        plt.title('Proportion of Rain Today (Yes vs No)')
        plt.ylabel('')  # Removes the y-label (it is not necessary for a pie chart)
        plt.show()
