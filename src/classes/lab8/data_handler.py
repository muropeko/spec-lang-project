from src.classes.lab8.graphs.histogram_graph import HistogramGraph
from src.classes.lab8.graphs.line_graph import LineGraph
from src.classes.lab8.graphs.bar_graph import BarGraph
from src.classes.lab8.graphs.scatter_graph import ScatterGraph
from src.classes.lab8.graphs.pie_graph import PieGraph
from src.classes.lab8.data_loader import DataLoader
from src.classes.lab8.graphs.combined_graphs import CombinedGraphs


class DataHandler:
    """
    A class responsible for loading data and creating various types of graphs.

    This class loads data from a specified file path and creates different kinds of visualizations
    such as histograms, line graphs, bar graphs, scatter plots, pie charts, and combined graphs.
    """

    def __init__(self, file_path):
        """
        Initializes the DataHandler with a DataLoader instance.

        Parameters:
            file_path (str): The path to the file containing data to be loaded.
        """
        self.loader = DataLoader(file_path)
        self.data = None

    def load_data(self):
        """
        Loads data using the DataLoader.

        This method retrieves the data and assigns it to the 'data' attribute.
        """
        self.data = self.loader.load_data()

    def create_all_graphs(self):
        """
        Creates all the graphs if the data is loaded.

        This method will create a histogram, line graph, bar graph, scatter plot, pie chart,
        and a combined graph.
        """
        if self.data is not None:
            self.create_histogram_graph()
            self.create_line_graph()
            self.create_bar_graph()
            self.create_scatter_graph()
            self.create_pie_graph()
            self.create_combined_graph()
        else:
            print("Data not loaded")

    def create_histogram_graph(self):
        """
        Creates a histogram graph for the data.
        """
        histogram = HistogramGraph(self.data)
        histogram.create_graph()

    def create_line_graph(self):
        """
        Creates a line graph for the data.
        """
        line_graph = LineGraph(self.data)
        line_graph.create_graph()

    def create_bar_graph(self):
        """
        Creates a bar graph for the data.
        """
        bar_graph = BarGraph(self.data)
        bar_graph.create_graph()

    def create_scatter_graph(self):
        """
        Creates a scatter plot for the data.
        """
        scatter_graph = ScatterGraph(self.data)
        scatter_graph.create_graph()

    def create_pie_graph(self):
        """
        Creates a pie chart for the data.
        """
        pie_graph = PieGraph(self.data)
        pie_graph.create_graph()

    def create_combined_graph(self):
        """
        Creates a combined graph with multiple visualizations.
        """
        combined_graphs = CombinedGraphs(self.data)
        combined_graphs.plot_combined_graphs()
