Glossary
========

- **Graph**: mathematical structures used to model pairwise relations between objects. A graph in this context is made up of vertices (also called nodes or points) which are connected by edges (also called links or lines).
|br|

- **Node**: vertice / point connected to another one by an edge / link.
|br|

- **Edge**: connection between nodes, with a head (origin node) and a tail (destination node).
|br|

- **Oriented Graph**: a graph where the edges have a given sense.
|br|

- **Cycle**: a cycle in a graph is a non-empty trail in which only the first and last vertices are equal.
|br|

- **Kernel**: in the case of an oriented graph, a kernel K is a subset/part of its nodes where the nodes have no edges connecting them 2 by 2 and each node not into K has at least 1 successor (targeted & linked edge) into K
|br|

- **Neighbor**:  out-neighbors / outgoing neighbors are vertices that have an edge from a vertex, and in-neighbors / incoming neighbors are vertices that have an edge to the vertex.
|br|

- **Dominance**: in graph theory, a node d dominates a node n if every path from the entry node to n must go through d. In the case of the Kern-Rowduction, a row r1 of a dataset dominates another one r2 if all the values of its columns are superior to the ones of r2.
|br|

- **Epsilon dominance**: identical to the oncept of dominance, but epsilon is a numerical number so that r2 > (1+epsilon) * r1 in order to be able to declare that r1 epsilon dominates r2.
|br|

- **Quasi Kernel**: an 'almost' kernel of a graph, which isn't stricly a kernel but close to it.
|br|

- **Kern Rowduction**: the whole process of the current package in order to undersample / reduce the number of rows of a given dataset.


.. |br| raw:: html

      <br