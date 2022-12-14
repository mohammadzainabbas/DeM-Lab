import sys

# ------------------------ #
# Helper logging functions
# ------------------------ #
def print_log(text: str) -> None:
    """
    Prints the log
    """
    print(f"[ log ]: {text}")

def print_error(text: str) -> None:
    """
    Prints the error
    """
    print(f"[ error ]: {text}")

if __name__ == "__main__":
    print_error("This is a module. Please import it.")
    sys.exit(1)

import numpy as np
from numpy import matrixlib as npmat
import networkx as nx
from typing import Union

# ------------------------ #
# Helper functions
# ------------------------ #
def csv_to_matrix(csv_file: str) -> npmat.matrix:
    """
    Returns a matrix from a csv file

    Parameters
    ----------
    csv_file: str
        Filename of the csv file
    
    Returns
    -------
    npmat.matrix
        A matrix
    """
    import pandas as pd
    return get_matrix_from_list(pd.read_csv(csv_file).values.tolist())

def excel_to_csv(filename: str) -> None:
    """
    Converts an excel file to a csv file

    Parameters
    ----------
    filename: str
        Filename of the excel file
    """
    import pandas as pd
    df = pd.read_excel(filename)
    df.to_csv(filename.replace(".xlsx", ".csv"), index=False)

# ------------------------ #
# Helper matrix functions
# ------------------------ #
def get_matrix(n_row: int = 5, n_col: int = 5, low: int = 2, seed: int = 0) -> npmat.matrix:
    """
    Returns a random matrix of a given size

    Parameters
    ----------
    n_row: int
        Number of rows
    n_col: int
        Number of columns
    low: int
        Lower bound of the random numbers
    seed: int
        Seed for the random number generator
    
    Returns
    -------
    npmat.matrix
        A random matrix
    
    Example
    -------
    >>> get_matrix(n_row=n_row, n_col=n_col, seed=0)
    matrix([[0, 1, 1, 0, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0],
            [0, 0, 0, 0, 1],
            [0, 1, 1, 0, 0]])
    """
    # np.random.seed(seed=seed)
    return npmat.asmatrix(np.random.randint(low, size=(n_row, n_col)))

def get_matrix_from_list(list_of_lists: list) -> npmat.matrix:
    """
    Returns a matrix from a list of lists

    Parameters
    ----------
    list_of_lists: list
        A list of lists
    
    Returns
    -------
    npmat.matrix
        A matrix
    
    Example
    -------
    >>> get_matrix_from_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])
    """
    return npmat.asmatrix(list_of_lists)

def numpy_matrix_to_network_graph(matrix: npmat.matrix) -> nx.Graph:
    """
    Convert from a numpy matrix to a network graph

    Parameters
    ----------
    matrix: npmat.matrix
        A numpy matrix
    
    Returns
    -------
    nx.Graph
        A network graph
    """
    return nx.from_numpy_matrix(matrix)

def plot_graph(graph: Union[npmat.matrix, nx.Graph], **kwargs: dict) -> None:
    """
    Plots a given graph/matrix

    Parameters
    ----------
    matrix: npmat.matrix or nx.Graph
        A numpy matrix or a network graph
    """
    if isinstance(graph, npmat.matrix):
        n_row, n_col = graph.shape
        if n_row != n_col:
            print_error(f"Adjacency matrix not square: nx,ny=({n_row}, {n_col}) [NetworkXError]")
            return
        graph = numpy_matrix_to_network_graph(graph)
    nx.draw(graph, with_labels=True, **kwargs)


"""

P1 - within 1 km radius

P2 - must visit effiel tower and catacombs

P3 - either visit Notre Dame Cathedral or Sainte Chapelle

P4 - must visit tour montparnasse

P5 - must visit the Pompidou Center if he visits Louvre

"""