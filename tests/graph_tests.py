from interactive_visualization.graph_utils import Graph, Arc


def test_graph_base():
    arcs = [
        Arc(0, 1, 2),
        Arc(1, 2, 3),
        Arc(2, 0, 2)
    ]
    # just check that no internal errors occur
    visualized = Graph(arcs).visualize()
    assert visualized is not None
