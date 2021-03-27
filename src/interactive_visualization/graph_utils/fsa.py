import openfst_python as fst
from .graph import Graph, Arc, Node

def draw_fsa(fsa, symbols=None):
    if fsa.input_symbols() is not None:
        symbols = fsa.input_symbols()
    arcs = []
    for state in fsa.states():
        for arc in fsa.arcs(state):
            symbol = str(symbols.find(arc.ilabel).decode('utf-8') if symbols else arc.ilabel)
            arcs.append(Arc(state, arc.nextstate, weight=symbol, 
                            attributes={"constraint": ("true" if arc.ilabel != 0 else "false"),
                                        "style": ("solid" if arc.ilabel != 0 else "dashed")}))
    
    graph = Graph(arcs)
    for id_, node in graph.nodes.items():
        if fsa.start() == id_:
            node.SetAttribute("style", "bold")
        if float(fsa.final(id_)) < float("Inf"):
            node.SetAttribute("shape", "doublecircle")
    return graph.Visualize()     
    