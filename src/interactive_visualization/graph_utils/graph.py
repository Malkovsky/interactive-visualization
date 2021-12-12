# Author Nikolay Malkovsky 2020-...

import graphviz


class Node:
    """
    Class for graph node representation, wrapper over graphviz node class,
    contains information on incident arcs and visualization attributes
    """
    def __init__(self, id: int):
        """
        Initialization with default visualization style (black solid circle)

        Args:
            id: unique integer identifier of a node
        """
        self.id = id
        self.arcs = []
        self.attributes = dict()
        self.SetColor('black')
        self.SetStyle('solid')
        self.SetShape('circle')

    def set_color(self, color: str):
        """
        Sets the color of a node to "color", see https://graphviz.org/docs/attrs/color/
        for more details

        Args:
            color: name of a color
        """
        self.attributes['color'] = color

    def set_style(self, style: str):
        """
        Sets the style of a node to "style", see https://graphviz.org/docs/attrs/style/
        for more details

        Args:
            style: name of a style
        """
        self.attributes['style'] = style

    def set_shape(self, shape):
        """
        Sets the shape of a node to "shape", see https://graphviz.org/docs/attrs/shape/
        for more details

        Args:
            shape: name of a shape
        """
        self.attributes['shape'] = shape

    def set_attribute(self, attr, value):
        """
        Sets the "attr" attribute of a node to "value", see https://graphviz.org/docs/attrs/
        for more details

        Args:
            attr: attribute name to set
            value: value to be assinged to attribute attr
        """
        self.attributes[attr] = value

    def SetColor(self, color):
        """
        Obsolette backward compativility function, use set_color instead
        """
        self.attributes['color'] = color

    def SetStyle(self, style):
        """
        Obsolette backward compativility function, use set_style instead
        """
        self.attributes['style'] = style

    def SetShape(self, shape):
        """
        Obsolette backward compativility function, use set_shape instead
        """
        self.attributes['shape'] = shape

    def SetAttribute(self, attr, value):
        """
        Obsolette backward compativility function, use set_attribute instead
        """
        self.attributes[attr] = value


class Arc:
    """
    Class for graph arc representation, wrapper over a graphviz arc,
    contains incident node information and visualization attributes
    """

    def __init__(self, from_, to_, weight=None, attributes=None):
        """
        Defines the arc going from node with id from_ to node with id to_ with optional
        weight "weight" and optional custom attribute dictionary passed to graphviz
        """
        self.beginning = from_
        self.end = to_
        self.weight = weight

        self.attributes = dict()
        self.attributes['color'] = 'black'
        self.attributes['style'] = 'solid'
        self.attributes['constraint'] = 'true'

        if attributes is not None:
            for key, value in attributes.items():
                self.attributes[key] = value

    def set_color(self, color):
        """
        Sets the color of arc to "color", see https://graphviz.org/docs/attrs/color/
        for more details

        Args:
            color: name of a color
        """
        self.attributes['color'] = color

    def set_style(self, style):
        """
        Sets the style of arc to "style", see https://graphviz.org/docs/attrs/style/
        for more details

        Args:
            style: name of a style
        """
        self.attributes['style'] = style

    def set_attribute(self, attr, value):
        """
        Sets the "attr" attribute of arc to "value", see https://graphviz.org/docs/attrs/
        for more details

        Args:
            attr: attribute name to set
            value: value to be assinged to attribute attr
        """
        self.attributes[attr] = value

    def SetColor(self, color):
        """
        Obsolette backward compativility function, use set_color instead
        """
        self.attributes['color'] = color

    def SetStyle(self, style):
        """
        Obsolette backward compativility function, use set_style instead
        """
        self.attributes['style'] = style

    def SetAttribute(self, attr, value):
        """
        Obsolette backward compativility function, use set_attribute instead
        """
        self.attributes[attr] = value


class Graph:
    """
    Class for graph representation, wrapper of graphviz digraph
    """

    def __init__(self, arcs=None):
        """
        Initializes a graph object

        Args:
            arcs: iterable object containing a set of "Arc" objects
        """
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

    def set_rank(self, node_id: int, rank_label):
        """
        Sets the rank of node with id node_id with rank_label
        for more information seee https://graphviz.org/docs/attrs/rank/
        Used for specifying the alignment of nodes

        Args:
            node_id: integer identifier of node
            rank_label: label to mark the node
        """
        if self.rank is None:
            self.rank = dict()
        self.rank[node_id] = rank_label

    def SetRank(self, node_id, rank_label):
        """
        Obsolette backward compatibility method, use set_rank instead
        """
        self.set_rank(node_id, rank_label)

    def add_arc(self, from_, to_, weight=None, attributes=None):
        """
        Add an arc from node with id from_ to node with id to_, optional weight
        and graphviz attributes
        """
        arc = Arc(from_, to_, weight, attributes.copy() if attributes is not None else None)
        self.nodes[from_].arcs.append(arc)

    def AddArc(self, from_, to_, weight=None, attributes=None):
        """
        Obsolette backward compatibility method, use set_rank instead
        """
        self.add_arc(from_, to_, weight, attributes)

    def expand_in_time(self, num):
        """
        Create an expanded in time version of the graph: in this graph there are num copies
        of initial graph with arcs going from copy i to copy i + 1

        Args:
            num: number of time copies of the graph

        Returns:
            Graph object representing expansion of self
        """
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
                result.SetRank(num_nodes, "t=" + str(i + 1))
                num_nodes += 1

            for node in self.nodes.values():
                for arc in node.arcs:
                    result.AddArc(prev[arc.beginning], cur[arc.end],
                                  attributes={"constraint": str(arc.beginning == arc.end)})

            prev = cur

        return result

    def visualize(self, dist=None, graph_attr={"rankdir": "LR"}):
        """
        Represent the graph as a graphviz.Digraph

        Args:
            dist: optional list of marks for nodes added to the id in visualization

        Returns:
            graphviz.Digraph object representing self
        """
        graph_repr = graphviz.Digraph(graph_attr=graph_attr, edge_attr={'arrowhead': 'vee'})
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
                with graph_repr.subgraph(name="cluster_" + group) as s:
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

    def Visualize(self, dist=None, graph_attr={"rankdir": "LR"}):
        """
        Obsolette backward compatibility method, use visualize instead
        """
        return self.visualize(dist, graph_attr)
