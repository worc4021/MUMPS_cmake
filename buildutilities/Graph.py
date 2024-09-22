from collections import OrderedDict

class Graph:
    def __init__(self):
        self.nodes = list()
        self.edges = {}
        self.comments = {}

    def add_node(self, node : str):
        if node not in self.nodes:
            self.nodes.append(node)
        if node not in self.edges:
            self.edges[node] = list()
        if node not in self.comments:
            self.comments[node] = ""

    def add_edge(self, node1 : str, node2 : str):
        self.add_node(node1)
        self.add_node(node2)
        self.edges[node1].append(node2)

    def has_node(self, node : str):
        return node in self.nodes
    
    def has_edge(self, node1 : str, node2 : str):
        return node1 in self.edges and node2 in self.edges[node1]

    def node_comment(self, node :str, msg :str):
        self.comments[node] = msg

    def __str__(self):
        res = ""
        for node in self.nodes:
            res += str(node) + " -> " + str(self.edges[node]) + "\n"
        return res

    def __repr__(self):
        return self.__str__()
    
    def toDOT(self) -> str:
        res = "digraph G {\n"
        res += " ranksep=.25;\n"
        res += " edge [arrowsize=.5]\n"
        res += " node [shape=ellipse, fontname=\"ArialNarrow\","
        res += " fontsize=12, fixedsize=false, height=.45];\n"
        for nodeId in range(len(self.nodes)):
            res += f' node{nodeId} [label="{self.nodes[nodeId]}", comment="{self.comments[self.nodes[nodeId]]}"];\n'
        res += "\n"
        for node1Id in range(len(self.nodes)):
            for node2 in self.edges[self.nodes[node1Id]]:
                res += f'  node{node1Id} -> node{self.nodes.index(node2)};\n'
        res += "}"
        return res
    
    def exportForMatlab(self) -> str:
        res = ""
        for nodeId in range(len(self.nodes)):
            res += f' node{nodeId} [label="{self.nodes[nodeId]}", comment="{self.comments[self.nodes[nodeId]]}"];\n'
        res += "\n"
        for node1Id in range(len(self.nodes)):
            for node2 in self.edges[self.nodes[node1Id]]:
                res += f'  node{node1Id} -> node{self.nodes.index(node2)};\n'
        return res

    def merge(self, other : 'Graph'):
        for node in other.nodes:
            self.add_node(node)
        for node in other.nodes:
            for edge in other.edges[node]:
                self.add_edge(node, edge)