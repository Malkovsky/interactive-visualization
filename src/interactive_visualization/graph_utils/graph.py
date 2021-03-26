import graphviz

class Node:
    def __init__(self, id):
        self.id = id
        self.arcs = []
        self.attributes = dict()
        self.SetColor('black')
        self.SetStyle('solid')
        self.SetShape('circle')

    def SetColor(self, color):
        self.attributes['color'] = color

    def SetStyle(self, style):
        self.attributes['style'] = style

    def SetShape(self, shape):
        self.attributes['shape'] = shape

    def SetAttribute(self, attr, value):
        self.attributes[attr] = value


class Arc:
    def __init__(self, from_, to_, weight=None, attributes = None):
        self.beginning = from_
        self.end = to_
        self.weight=weight

        self.attributes = dict()
        self.attributes['color'] = 'black'
        self.attributes['style'] = 'solid'
        self.attributes['constraint'] = 'true'
        
        if attributes is not None:
            for key, value in attributes.items():
                self.attributes[key] = value

    def SetColor(self, color):
        self.attributes['color'] = color

    def SetStyle(self, style):
        self.attributes['style'] = style

    def SetAttribute(self, attr, value):
        self.attributes[attr] = value

class Graph:
    def __init__(self, arcs=None):
        self.nodes = dict()
        self.rank = None
        if arcs is not None:
            for arc in arcs:
                if arc.beginning not in self.nodes:
                    self.nodes[arc.beginning] = Node(arc.beginning)
                if arc.end not in self.nodes:
                    self.nodes[arc.end] = Node(arc.end)
                self.AddArc(arc.beginning, arc.end, arc.weight, arc.attributes)

    # def AddNode(self):
    #     num_nodes = len(self.nodes)
    #     self.nodes.append(Node(num_nodes))
    
    def SetRank(self, node_id, rank_label):
        if self.rank is None:
            self.rank = dict()
        self.rank[node_id] = rank_label

    def AddArc(self, from_, to_, weight=None, attributes=None):
        arc = Arc(from_, to_, weight, attributes.copy() if attributes is not None else None)        
        self.nodes[from_].arcs.append(arc)
        
    def expand_in_time(self, num):
        result = Graph()
        num_nodes = 0
        prev = dict()
    
        for node_id in self.nodes:
            result.nodes[num_nodes] = Node(num_nodes)
            prev[node_id] = num_nodes
            result.SetRank(num_nodes, "t=0")
            num_nodes += 1
        for i in range(num):
            cur = dict()
            for node in self.nodes.values():
                result.nodes[num_nodes] = Node(num_nodes)
                cur[node.id] = num_nodes
                result.SetRank(num_nodes, "t="+str(i+1))
                num_nodes += 1

            for node in self.nodes.values():
                for arc in node.arcs:
                    result.AddArc(prev[arc.beginning], cur[arc.end], attributes={"constraint":str(arc.beginning==arc.end)})
        
            prev = cur

        return result

    def Visualize(self, dist=None):
        graph_repr = graphviz.Digraph(graph_attr={"rankdir" : "LR"}, edge_attr={'arrowhead':'vee'})
        attrs = {}
        if self.rank is None:
            for id_, node in self.nodes.items():
                graph_repr.node(str(id_), str(id_) + ("" if dist is None else ("/" + str(dist[id_]))), 
                                color=node.attributes['color'], 
                                style=node.attributes['style'],
                                shape=node.attributes['shape'])
        else:
            rank_groups = dict()
            for node_id in self.nodes:
                if node_id in self.rank:
                    rank = self.rank[node_id]
                    if rank not in rank_groups:
                        rank_groups[rank] = []
                    rank_groups[rank].append(node_id)
            for group, nodes in rank_groups.items():
                with graph_repr.subgraph(name="cluster_"+group) as s:
                    s.attr(label=group)
                    s.attr(rank="same")
                    for id_ in nodes:
                        node = self.nodes[node_id]
                        s.node(str(id_), str(id_) + ("" if dist is None else ("/" + str(dist[id_]))), 
                               color=node.attributes['color'], 
                               style=node.attributes['style'],
                               shape=node.attributes['shape'])
        
        for id_, node in self.nodes.items():
            for arc in node.arcs:
                graph_repr.edge(str(node.id),
                                str(arc.end),
                                label="" if arc.weight is None else str(arc.weight),
                                color=arc.attributes['color'],
                                style=arc.attributes['style'],
                                constraint=arc.attributes['constraint'])
        return graph_repr