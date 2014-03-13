# Natural Language Toolkit: code_networkx

'''
Example 4.15 from Section 4.8.2: NetworkX
Figure 4.15: Using the NetworkX and Matplotlib Libraries

initializes an empty graph (3) then [recursively] traverses the WordNet hypernym hierarchy adding edges to the graph (1).
Notice that the traversal is recursive (2)

Had to install:
- networkx
- pygraphviz

Still gives random errors in Windows about graphviz not being installed
- http://stackoverflow.com/questions/4571067/installing-pygraphviz-on-windows/7537047#7537047
- http://pygraphviz.github.io/documentation/latest/reference/faq.html
- screw it, just try it in Linux
'''


import networkx as nx
import matplotlib
from nltk.corpus import wordnet as wn

def traverse(graph, start, node):
    graph.depth[node.name] = node.shortest_path_distance(start)
    for child in node.hyponyms():
        graph.add_edge(node.name, child.name)                   # (1) add edges from here    
        traverse(graph, start, child)                           # (2) recurse!

def hyponym_graph(start):
    G = nx.Graph()                                              # (3) initialize empty graph    
    G.depth = {}
    traverse(G, start, start)
    return G

def graph_draw(graph):
    nx.draw_graphviz(graph,
         node_size = [16 * graph.degree(n) for n in graph],
         node_color = [graph.depth[n] for n in graph],
         with_labels = False)
    matplotlib.pyplot.show()


if __name__ == "__main__":
    print __doc__
    dog = wn.synset('dog.n.01')
    graph = hyponym_graph(dog)
    graph_draw(graph)