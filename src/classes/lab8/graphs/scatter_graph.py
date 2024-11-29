import matplotlib.pyplot as plt
import seaborn as sns
from src.classes.lab8.graph_template import GraphTemplate


class ScatterGraph(GraphTemplate):
    """
    A class to create a scatter plot showing the relationship between 'MaxTemp' (maximum temperature)
    and 'Rainfall' (precipitation) with different colors based on 'RainToday' (whether it rained today).

    Inherits from GraphTemplate and overrides methods to set up the data and plot the scatter graph.
    """

    def setup_data(self):
        """
        Prepares the data for plotting by selecting relevant columns:
        'MaxTemp' (maximum temperature), 'Rainfall' (precipitation), and 'RainToday' (whether it rained today).

        :return: None
        """
        self.data_to_plot = self.data[['MaxTemp', 'Rainfall', 'RainToday']]

    def plot_graph(self):
        """
        Plots a scatter graph showing the relationship between 'MaxTemp' and 'Rainfall' and colors
        the points based on 'RainToday' values.

        - Uses the 'MaxTemp' for the x-axis and 'Rainfall' for the y-axis.
        - Colors the points according to 'RainToday' values with a color palette ('coolwarm').
        - Adds titles, labels, and displays the graph.

        :return: None
        """
        plt.figure(figsize=(8, 6))
        sns.scatterplot(data=self.data_to_plot, x='MaxTemp', y='Rainfall', hue='RainToday', palette='coolwarm')
        plt.title('Max Temperature vs Rainfall')
        plt.xlabel('Max Temperature (°C)')
        plt.ylabel('Rainfall (mm)')
        plt.show()
