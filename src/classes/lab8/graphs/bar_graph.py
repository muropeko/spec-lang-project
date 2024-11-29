import matplotlib.pyplot as plt
from src.classes.lab8.graph_template import GraphTemplate

class BarGraph(GraphTemplate):
    """
    A class for creating bar graphs based on the 'RainToday' column in the dataset.

    This class inherits from GraphTemplate and is responsible for creating a bar graph
    showing the number of days with rain and without rain (Yes vs No) in the dataset.
    """

    def setup_data(self):
        """
        Prepares the data to be plotted.

        This method calculates the value counts of the 'RainToday' column and stores
        the results in the `data_to_plot` attribute for later use in the plot.
        """
        self.data_to_plot = self.data['RainToday'].value_counts()

    def plot_graph(self):
        """
        Plots the bar graph using the prepared data.

        This method creates a bar graph that visualizes the distribution of 'RainToday' values
        (Yes vs No), with 'skyblue' and 'orange' colors for the bars. It also sets the title,
        axis labels, and formats the x-ticks.
        """
        plt.figure(figsize=(8, 6))
        self.data_to_plot.plot(kind='bar', color=['skyblue', 'orange'])
        plt.title('Rain Today (Yes vs No)')
        plt.xlabel('Rain Today')
        plt.ylabel('Number of Days')
        plt.xticks(rotation=0)
        plt.show()
