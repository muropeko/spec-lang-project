from abc import ABC, abstractmethod


class GraphTemplate(ABC):
    """
    A template class for creating different types of graphs.
    This class defines the general steps for creating a graph,
    but the specifics of data setup and graph plotting are
    delegated to subclasses that implement the abstract methods.
    """

    def __init__(self, data):
        """
        Initializes the graph template with the given data.

        Parameters:
            data (pandas.DataFrame): The data to be used for graph creation.
        """
        self.data = data

    def create_graph(self):
        """
        The template method that defines the general sequence of operations
        for creating a graph: setting up the data and plotting the graph.

        This method calls the abstract methods `setup_data` and `plot_graph`,
        which must be implemented in the subclass.
        """
        self.setup_data()
        self.plot_graph()

    @abstractmethod
    def setup_data(self):
        """
        Abstract method to set up the data for the graph.

        Subclasses should implement this method to prepare the data
        according to the specific requirements of the graph.

        This method will be called by `create_graph` before plotting.
        """
        pass

    @abstractmethod
    def plot_graph(self):
        """
        Abstract method to plot the graph using the prepared data.

        Subclasses should implement this method to generate the actual plot.
        This method will be called by `create_graph` after the data setup.
        """
        pass
