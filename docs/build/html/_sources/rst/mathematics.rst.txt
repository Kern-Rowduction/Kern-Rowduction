Mathematical concepts
=====================

Knowledges about Graphs
-----------------------


General Intuition
-----------------

The idea behind the Kern-Rowduction algorithm is to represent a dataset as an oriented graph of nodes and to find its more 'core' characteristics, that is to say its kernel.
Thus, it removes the 'useless' & 'noisy' data instances/rows and increases the variance of the dataset / potential machine learning models. 

Another way to understand the intuition is to imagine the case of a Multi-objective optimization. For example, if you’re looking for a good car with the best 
quality / price ratio and there are plenty of cars that are proposed, a way to visualize the problem is to:

- Draw a graph with the price & the quality as axis
- Put all the cars as points on the axis according to their price and quality measured
- Remove all dominated points. But you can still have an infinite number of potential cars that are not pairwise dominant. So the main problem is how to choose between all this large number of choices that can’t dominate each other (called the ‘representativeness problem’). The idea is to gather them into small clusters - each cluster is made up of very similar points - and then reduce the number of points in each cluster by keeping the point(s) that best represent(s) the main characteristics of that cluster (generally the barycentre and the convex envelope). In other words, it is like finding the skeleton of a complex body / shape.
- This way you are sure that all the main combinations of price/quality are represented by at least one point (car)

Below the representation into a graph of the problem with the cars previously explained:

.. figure:: /img/dominance_intuition_graph.png
   :scale: 75 %
   :alt: Scheme/Graph to show visually the intuition of dominance between items/cars/nodes.



Thus, the Kern-Rowduction tries to grasp the same intuition used to solve the 'representativeness problem': we try to reduce the number of the observations on the data set using the same approach (gathering points into small clusters that are going to be represented by fewer points) through graphs and kernels. 
It is explained furthermore in the next section below.

Approach
--------

1. Convert the input dataset into an oriented graph:

    - Each observation will be represented by a vertice which will have the same number as the row index and we will add an edge between two vertices whenever an observation epsilon-dominate another one.
    - Epsilon-domination is a relaxation of standard domination. We can say that vertice X epsilon-dominates the vertice Y if and only if X > (1+epsilon)*Y, that is to say if each coordinate/feature of the row X is superior to (1+epsilon) times the same coordinate/feature of the row Y. 

2. Ideally, one would like to find the kernel directly. However, any graph can either have no kernel or have an infinite number of kernels or a finite number of them. Thus, the idea is to find its quasi-kernel. To do this, we must start by separating the graph into 2 induced sub-graphs without circuits.
3. To create the 2 induced sub-graphs and to make sure they are circuitless, we proceed as follows:

    The 2 sub-graphs will have all the vertices from the original graph, then we will split the edges between them as follows:

        a. If the number associated to the source vertice is higher that the number associated to the destination vertice, then the edge will be added to the first subgraph.
        b. If not then the edge will be added to the second subgraph.

4. We will compute the kernel of the first subgraph (there is one and only one kernel for a circuitless graph). Then, we will create a new graph that will have the vertices of the kernel that we just compute but the edges of the second subgraph. Finally, we compute the kernel of that last created graph and the vertices of this last kernel (also named quasi-kernel of the original graph) will be the observations that we will keep from our dataset.

More information
----------------

A deeper explanation of the Kern Rowduction package and methodology will come later, notably with a scientific publication.

