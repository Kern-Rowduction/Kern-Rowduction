"""All the usable methods/functions which constitute the Kern_Rowduction package."""

import pandas as pd
import numpy as np
import networkx as nx
from tqdm import tqdm

def epsilon_dominates(point_id_1=int, point_id_2=int, df=pd.DataFrame, epsilon=float):
    '''From an input DF, check if the input node Point 1 (row 1) epsilon dominates the node
        Point 2 (row 2).

    Parameters
    ----------
    point_id_1 : int
        Row index of the point 1 in the pandas DataFrame df
    point_id_2 : int
        Row index of the point 2 in the pandas DataFrame df
    df : pd.DataFrame
        Pandas Dataframe where the point are stored
    epsilon : float
        Threshold of dominance between 2 points: Point1 must be > (1+epsilon)*Point2 for each column

    Returns
    -------
    flag
        A boolean which is True if Point 1 epsilon dominates Point 2 otherwise False
    '''

    flag = True #Assumed true unless evidence to the contrary

    # Get all the edged nodes of Point 1 & 2
    point_1 = list(df.iloc[point_id_1])
    point_2 = list(df.iloc[point_id_2])

    # Iteration over each edged node of Point 1
    for i in range(len(point_1)):
        if point_1[i] > (1+epsilon)*point_2[i]:
            flag = False
            break

    return flag # True if Point 1 epsilon dominates Point 2 otherwise False

def find_in_neighbors(graph, point_id, all_neighbors_dic):
    '''From a graph and a dictionary of all nodes' neighbors, find all INNER neighbors of
       the input node (identified by its point_id).

    Parameters
    ----------
    graph : networkx DiGraph
        Networkx Digraph with all the nodes and edges created basically from the original DataFrame
    point_id : int
        Number ID of the node to analyze in the graph
    all_neighbors_dic : dict
        Dictionary of integers (nodes) with all the inner and outer neighbors of the all the nodes

    Returns
    -------
    in_neighbors : list
        A list with all the INNER neighbords of the node point_id
    '''
    all_neighbors = all_neighbors_dic[point_id] # Neighbors of point_id
    in_neighbors = []
    # For all the edged node IDs in the dictionary for the input node
    for neighbor in all_neighbors:
        #If there is an edge TO the input node, append it to the list of all INNER neighbors
        if (neighbor, point_id) in graph.edges():
            in_neighbors.append(neighbor)
    return in_neighbors

def find_out_neighbors(graph, point_id, all_neighbors_dic):
    '''From a graph and a dictionary of all nodes' neighbors, find all OUTER neighbors of
       the input node (identified by its point_id).

    Parameters
    ----------
    graph : networkx DiGraph
        Networkx Digraph with all the nodes and edges created basically from the original DataFrame
    point_id : int
        Number ID of the node to analyze in the graph
    all_neighbors_dic : dict
        Dictionary of integers (nodes) with all the inner and outer neighbors of the all the nodes

    Returns
    -------
    in_neighbors : list
        A list with all the OUTER neighbords of the node point_id
    '''
    all_neighbors = all_neighbors_dic[point_id] # Neighbors of point_id
    out_neighbors = []
    # For all the edged node IDs in the dictionary for the input node
    for neighbor in all_neighbors:
        #If there is an edge FROM the input node, append it to the list of all OUTER neighbors
        if (point_id, neighbor) in graph.edges():
            out_neighbors.append(neighbor)
    return out_neighbors

def extract_kernel(graph, all_neighbors_dic):
    '''Retrieve the kernel of the input directed graph if there is one.
        NB : This function works indefinitely if the graph includes a circuit.

    Parameters
    ----------
    graph : networkx DiGraph
        Networkx Digraph with all the nodes and edges created basically from the original DataFrame
    all_neighbors_dic : dict
        Dictionary of integers (nodes) with all the inner and outer neighbors of the all the nodes

    Returns
    -------
    kernel : list
        A sorted list with all the nodes of the kernel computed.
    '''
    # Initialize variables
    kernel = []
    nodes = graph.nodes()

    # Initialize list of nodes to check
    d_minus, candidate = {}, {}
    for i in nodes:
        d_minus[i] = 0
        candidate[i] = False

    # Iteration over each node of the graph
    for x in nodes:
        d_minus[x] = len(find_in_neighbors(graph, x, all_neighbors_dic))
        if d_minus[x] == 0: # If the node has no previous one, it's added to the kernel
            kernel.append(x)
        else: # Otherwise it is added as a potential candidate to check as kernel's
                # node by the search algorithm
            candidate[x] = True

    nb_candidates = sum([candidate[key] for key in candidate])

    # Search algorithm : Check if the candidates are kernel's node or not
    # So long there is still at least 1 remaining candidate node
    while nb_candidates > 0:

        # For each node x in the kernel
        for x in kernel:
            # For each OUT neighbors of this node X
            for y in find_out_neighbors(graph, x, all_neighbors_dic):

                # If the found OUT neighbor node Y is also a candidate ==> we remove it
                    # from the list of candidates
                if candidate[y]:
                    candidate[y] = False
                    nb_candidates -= 1

                    # For each OUT neighbors of this IN neighbor node Y
                    for z in find_out_neighbors(graph, y, all_neighbors_dic):

                        if candidate[z]: # If the found OUT neighbor node Z of Y
                                            # is a remaining candidate, remove it
                            d_minus[z] -= 1
                            if d_minus[z] == 0: # If it's the last node, then there is no
                                                    # following nodes, so append it to the kernel
                                kernel.append(z)
                                candidate[z] = False
                                nb_candidates -= 1

    # Return the final computed kernel
    return sorted(kernel)

def build_uncycled_subgraphs(graph):
    '''Build 2 induced subgraphs from the input graph so that both subgraphs don't include cycles.
       That is to say, from a input graph, build 2 sub graphs according to the sense of their edges
       (departure_node's value <=> arrival_node's value).

    Parameters
    ----------
    graph : networkx DiGraph
        Networkx Digraph with all the nodes and edges created basically from the original DataFrame

    Returns
    -------
    graph1_prime : networkx DiGraph
        A uncycled sub graph with the edges between a lower node's value to a higher node's value
        from the input graph
    graph2_prime : networkx DiGraph
        A uncycled sub graph with the other edges from the input graph not put into graph1_prime
    '''

    # Make the 2 subgraphs with the same nodes
    graph1_prime = nx.DiGraph()
    graph1_prime.add_nodes_from(list(graph.nodes))
    graph2_prime = nx.DiGraph()
    graph2_prime.add_nodes_from(list(graph.nodes))

    # Copy the edges of the input graph in one or another subgraph according to the values
        # of the entry/exit nodes
    for e in graph.edges():
        if e[0] < e[1]: # If the entry node's value < exit node's value ==> add the
                            # edge to the subgraph 1
            graph1_prime.add_edge(e[0], e[1])
        else: # Otherwise ==> add the edge of the subgraph 2
            graph2_prime.add_edge(e[0], e[1])

    return graph1_prime, graph2_prime

def extract_quasi_kernel(uncycled_subgraph_1, uncycled_subgraph_2, all_neighbors_dic):
    '''Extract the quasi kernel from 2 associated uncycled subgraphs.

    Parameters
    ----------
    uncycled_subgraph_1 : networkx DiGraph
        Networkx Digraph without cycles and with all the nodes and "increasing" edges extracted
        initially from a bigger input graph.
    uncycled_subgraph_2 : networkx DiGraph
        Networkx Digraph without cycles and with all the nodes and "decreasing" edges extracted
        initially from a bigger input graph.
    all_neighbors_dic : dict
        Dictionary of integers (nodes) with all the inner and outer neighbors of the all the nodes

    Returns
    -------
    quasi_kernel : list
        A sorted list with all the nodes of the quasi kernel computed.
    '''

    subgraph_2_kernel = extract_kernel(uncycled_subgraph_1, all_neighbors_dic)
    subgraph_2_prime = uncycled_subgraph_2.subgraph(subgraph_2_kernel)
    quasi_kernel = extract_kernel(subgraph_2_prime, all_neighbors_dic)
    return quasi_kernel

def apply_kern_rowduction(df, epsilon, nb_rows_memory=100000, remove_isolated_points=False):
    '''Apply the "Rowduction" process on a DF and returns the reduced DataFrame.
        NB : The Rowduction process consists in building a directed graph, extracting its quasi
        kernel and returning the associated DF.

    Parameters
    ----------
    df : pandas DataFrame
        DataFrame to reduce through the "Rowduction" process
    epsilon : float
        Threshold of dominance between 2 points: Point1 must be > (1+epsilon)*Point2 for each column
    nb_rows_memory : int
        Number of rows per batch to process the Rowduction. Smaller it is, less memory it takes but
        potentially slower it is
    remove_isolated_points : boolean
        Enabled/Disabled the remove of the 'isolated' points/nodes in the graph, that is to say
        the nodes for which no epsilon dominance relationship has been found.

    Returns
    -------
    rowducted_df : pandas DataFrame
        The input 'df' DataFrame but rowducted, with only the rows to keep after the Rowduction
    '''

    # Initialize an empty DiGraph and all variables
    graph = nx.DiGraph() # Creation of a directed graph
    edges_list = []
    nodes_list = [row_index for row_index in df.index] # Nodes to add in the graph

    all_neighbors_dic = {} #Dictionary of nodes' neighbors

    # Compare each row of df with all of eps_df
    epsilon_prime = -1 + (1+epsilon)**0.5
    eps_df = (1+epsilon_prime)*df
    eps_df_array = np.array(eps_df.values[:, None])

    # For each subframe of the dataframe, we retrieve all epsilon dominated/dominating nodes
        # in a list of dict
    nb_iter = (len(df) // nb_rows_memory) + 1
    df_res = pd.DataFrame([], columns=['A', 'B'])
    for i in range(0, nb_iter):
        df_array = np.array(df.loc[i*nb_rows_memory : (i+1)*nb_rows_memory, :].values)
        all_greater = (eps_df_array >= df_array).all(axis=2) # It works because of the broadcast
                                                                # property of numpy arrays
        # Get the row indexes of df and eps_df where there is a epsilon dominance
            # thanks nonzero and transpose
        trans_greater = np.transpose(np.nonzero(all_greater))
        trans_greater[:, 1] += i*nb_rows_memory
        df_i = pd.DataFrame(trans_greater, columns=['A', 'B'])
        df_res = df_res.append(df_i)
        # Remove the self indexes (0 epsilon dominates 0 etc...)
        # And put into a dictionary the row indexes which are epsilon dominating or dominated
        df_res = df_res.drop_duplicates().reset_index(drop=True)
        dict_dominating = df_res[df_res['A'].ne(df_res['B'])].groupby('A')['B'].agg(list).to_dict()
        dict_dominated = df_res[df_res['A'].ne(df_res['B'])].groupby('B')['A'].agg(list).to_dict()

    # Merge both dominating & dominated nodes dictionaries + create the list of edges (as tuples)
    for k in df.index:
        node_doms = []
        edges = []

        if k in dict_dominated:
            node_doms.extend(dict_dominated[k])

            # Add edges to the edges_list
            edges = list(map(lambda x: (k, x), dict_dominated[k]))
            edges_list.extend(edges)

        if k in dict_dominating:
            node_doms.extend(dict_dominating[k])

        # Remove duplicates and add to the neighbor dictionary all merged dominated/dominating nodes
        node_doms = list(dict.fromkeys(node_doms))
        node_doms.sort()
        all_neighbors_dic[k] = node_doms

        del node_doms, edges

    # Build the global graph

        # Add all nodes
    if not remove_isolated_points:
        graph.add_nodes_from(nodes_list) # Can be deleted if you wish to remove 'pseudo outliers'

        # Add all edges of dominance relationships
    graph.add_edges_from(edges_list)

    # Compute quasi kernel
    graph_1_prime, graph_2_prime = build_uncycled_subgraphs(graph)
    quasi_kernel = extract_quasi_kernel(graph_1_prime, graph_2_prime, all_neighbors_dic)

    rowducted_df = df.iloc[quasi_kernel]
    return rowducted_df

def rowduct(df=pd.DataFrame, rowduction_target="all", epsilon=0.025, nb_rows_memory=10000, \
    step_activated=False, label_col="_krd_default_label_", rowduction_method="separately", \
    remove_isolated_points=False):
    '''Parametrize the "Rowduction" process, apply it on a DF and returns the reduced DataFrame.

    Parameters
    ----------
    df : pandas DataFrame
        DataFrame to reduce through the "Rowduction" process
    rowduction_target : list or str
        List of label values upon which to apply the Rowduction process. Rows with label values
        that are not listed will remain intact. If the rowduction_target = "all" (default value),
        the whole input DataFrame df is reduced.
    epsilon : float
        Threshold of dominance between 2 points: Point1 must be > (1+epsilon)*Point2 for each column
    nb_rows_memory : int
        Number of rows per batch to process the Rowduction. Smaller it is, less memory it takes but
        potentially slower it is
    step_activated : boolean
        True if the Rowduction has to be step by step of rows, which avoids memory errors in case of
        huge input DataFrame df. Otherwise False for a 'one shot' rowduction.
    label_col : str
        Name of the label column which contains the 'rowduction_target'
    rowduction_method : str
        Rowduction method : 'grouped' to reduce/rowduct together all Rowduction targets,
        'separately' to reduce/rowduct each of them separately and then concatenate them together
    remove_isolated_points : boolean
        Enabled/Disabled the remove of the 'isolated' points/nodes in the graph, that is to say
        the nodes for which no epsilon dominance relationship has been found.

    Returns
    -------
    rowducted_df : pandas DataFrame
        The input 'df' DataFrame but rowducted, with only the rows to keep after the Rowduction
    '''

    # If label_col is equal to the default value, \
    # then create a tempory constant column "_krd_default_label_"
    if label_col == "_krd_default_label_":
        df["_krd_default_label_"] = 0

    # If the rowduction target is "all", the target are the list of distinct values of the label_col
    if rowduction_target == "all":
        rowduction_target = list(set(df[label_col]))

    header = df.columns
    nb_iter = (len(df) // nb_rows_memory) + 1

    # If we want to do a step by step rowduction
    if step_activated and nb_iter > 1:


        # Initialize the dataframe concatenating the results of the various rowductions
        all_rd_data = pd.DataFrame([], columns=header)

        # For each batch of data with initialization the progress bar displayed in the console
        for i in tqdm(range(nb_iter), desc='... Kern Rowduction - Progression (by batch)'):

            index_begin = i*nb_rows_memory
            index_end = (i+1)*nb_rows_memory-1

            # Rowduct all values of the label together (0 and 1 together by example)
            if rowduction_method == "grouped":
                data = df.loc[index_begin:index_end].reset_index(drop=True)
                data_target = data[data[label_col].isin(rowduction_target)].reset_index(drop=True)
                rd_data_target = apply_kern_rowduction(data_target, epsilon,\
                    nb_rows_memory=nb_rows_memory, \
                    remove_isolated_points=remove_isolated_points)
                data_rest = data[~data[label_col].isin(rowduction_target)].reset_index(drop=True)
                rd_data = rd_data_target.append(data_rest).sample(frac=1).reset_index(drop=True)
                all_rd_data = all_rd_data.append(rd_data)
                del rd_data, data, data_target, data_rest, rd_data_target


            # Rowduct all values of the label separately, and then join them together
                # with the none rowducted ones
            elif rowduction_method == "separately":
                data = df.loc[index_begin:index_end].reset_index(drop=True)
                data_target = data[data[label_col].isin(rowduction_target)].reset_index(drop=True)
                data_rest = data[~data[label_col].isin(rowduction_target)].reset_index(drop=True)
                rd_data = data_rest.copy()
                for target in rowduction_target:
                    iter_data_target = data_target[data_target[label_col] == target]
                    iter_data_target = iter_data_target.reset_index(drop=True)
                    iter_rd_data_target = apply_kern_rowduction(iter_data_target, epsilon, \
                        nb_rows_memory=nb_rows_memory, \
                        remove_isolated_points=remove_isolated_points)
                    rd_data = rd_data.append(iter_rd_data_target)
                rd_data = rd_data.sample(frac=1).reset_index(drop=True)
                all_rd_data = all_rd_data.append(rd_data)
                del rd_data, data, data_target, data_rest, iter_data_target, iter_rd_data_target

            else:
                return "Error : bad rowduct_target input."


        # At the end rowduct all the rowducted data once again

        all_rd_data = all_rd_data.reset_index(drop=True)

        # Rowduct all values of the label together (0 and 1 together by example)
        if rowduction_method == "grouped":
            all_data_target = all_rd_data[all_rd_data[label_col].isin(rowduction_target)]
            all_data_target = all_data_target.reset_index(drop=True)
            all_rd_data_target = apply_kern_rowduction(all_data_target, epsilon, \
                nb_rows_memory=nb_rows_memory,\
                remove_isolated_points=remove_isolated_points)
            all_data_rest = all_rd_data[~all_rd_data[label_col].isin(rowduction_target)]
            all_data_rest = all_data_rest.reset_index(drop=True)
            final_rd_data = all_rd_data_target.append(all_data_rest)
            final_rd_data = final_rd_data.sample(frac=1).reset_index(drop=True)

            # If label_col is equal to the default value, \
            # then delete the temporary column "_krd_default_label_" previously created
            if label_col == "_krd_default_label_":
                final_rd_data = final_rd_data.drop('_krd_default_label_', axis=1)

            return final_rd_data

        # Rowduct all values of the label separately, and then join them together
            # with the none rowducted ones
        if rowduction_method == "separately":
            all_data_target = all_rd_data[all_rd_data[label_col].isin(rowduction_target)]
            all_data_target = all_data_target.reset_index(drop=True)
            all_data_rest = all_rd_data[~all_rd_data[label_col].isin(rowduction_target)]
            all_data_rest = all_data_rest.reset_index(drop=True)
            final_rd_data = all_data_rest.copy()

            for target in rowduction_target:
                iter_data_target = all_data_target[all_data_target[label_col] == target]
                iter_data_target = iter_data_target.reset_index(drop=True)
                iter_rd_data_target = apply_kern_rowduction(iter_data_target, epsilon,\
                    nb_rows_memory=nb_rows_memory,\
                    remove_isolated_points=remove_isolated_points)
                final_rd_data = final_rd_data.append(iter_rd_data_target)
                final_rd_data = final_rd_data.sample(frac=1).reset_index(drop=True)

            # If label_col is equal to the default value, \
            # then delete the temporary column "_krd_default_label_" previously created
            if label_col == "_krd_default_label_":
                final_rd_data = final_rd_data.drop('_krd_default_label_', axis=1)

            return final_rd_data

    # Else rowduct the whole dataset in one batch
    else:

        print('... Kern Rowduction - In Progression (1 batch) ...')

        # Rowduct all values of the label together (0 and 1 together by example)
        if rowduction_method == "grouped":
            data_target = df[df[label_col].isin(rowduction_target)].reset_index(drop=True)
            rd_data_target = apply_kern_rowduction(data_target, epsilon,\
                nb_rows_memory=nb_rows_memory,\
                remove_isolated_points=remove_isolated_points)
            data_rest = df[~df[label_col].isin(rowduction_target)].reset_index(drop=True)
            rd_data = rd_data_target.append(data_rest)
            rd_data = rd_data.sample(frac=1).reset_index(drop=True)

            # If label_col is equal to the default value, \
            # then delete the temporary column "_krd_default_label_" previously created
            if label_col == "_krd_default_label_":
                rd_data = rd_data.drop('_krd_default_label_', axis=1)

            return rd_data

        # Rowduct all values of the label separately, and then join them together
            # with the none rowducted ones
        if rowduction_method == "separately":
            data_target = df[df[label_col].isin(rowduction_target)].reset_index(drop=True)
            data_rest = df[~df[label_col].isin(rowduction_target)].reset_index(drop=True)
            rd_data = data_rest.copy()

            for target in rowduction_target:
                iter_data_target = data_target[data_target[label_col] == target]
                iter_data_target = iter_data_target.reset_index(drop=True)
                iter_rd_data_target = apply_kern_rowduction(iter_data_target, epsilon,\
                    nb_rows_memory=nb_rows_memory, \
                    remove_isolated_points=remove_isolated_points)
                rd_data = rd_data.append(iter_rd_data_target)
            rd_data = rd_data.sample(frac=1).reset_index(drop=True)

            # If label_col is equal to the default value, \
            # then delete the temporary column "_krd_default_label_" previously created
            if label_col == "_krd_default_label_":
                rd_data = rd_data.drop('_krd_default_label_', axis=1)

            return rd_data

        else:
            return "Error : bad rowduct_target input."
