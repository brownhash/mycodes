class Graph:
    def __init__(self):
        self.node = []
        self.connections = {}

    def addnode(self, node):
        self.node.append(node)

    def connect(self, node1, node2, weight):
        if type(weight).__name__ != "int" and type(weight).__name__ != "float":
            raise Exception("Weight can only be a integer value and not {}".format(type(weight).__name__))
        if node1 in self.node and node2 in self.node:
            if node1 in self.connections:
                all_nodes = self.connections.get(node1)
                all_nodes[node2] = weight
            else:
                self.connections[node1] = {node2: weight}
            if node2 in self.connections:
                all_nodes = self.connections.get(node2)
                all_nodes[node1] = weight
            else:
                self.connections[node2] = {node1: weight}
        else:
            raise Exception("{} - {} is not a valid path".format(node1, node2))

    def pathweight(self, node1, node2):
        if node1 in self.connections and node2 in self.connections:
            connection1 = self.connections.get(node1)
            if node2 in connection1:
                return connection1.get(node2)
            else:
                raise Exception("{} & {} are not connected".format(node1, node2))
        else:
            raise Exception("{} - {} is not a valid path".format(node1, node2))

    def connection(self, node):
        if node in self.connections:
            result = []
            for connection_nodes in self.connections.get(node):
                result.append(connection_nodes)
            return result
        else:
            raise Exception("{} is not a valid node".format(node))

    def connectionmap(self, node):
        if node in self.connections:
            return self.connections.get(node)
        else:
            raise Exception("{} is not a valid node".format(node))

    def nodes(self):
        return self.node

    def __str__(self):
        return self.__class__.__name__

# Using Graph -
# 1. Create isinstance
#     graph = Graph()
# 2. Add nodes
#     graph.addnode("Node1")
#     graph.addnode("Node1")
# 3. Connect nodes with a weight of their path
#     graph.connect("Node1", "Node2", 2)
# 4. Get path weight of 2 nodes
#     graph.pathweight("Node1", "Node2")
# 5. Get connected nodes
#     graph.connection("Node1")
# 6. Get connected nodes with distance
#     graph.connectionmap("Node1")
# 7. Get all added nodes
#     graph.nodes()
