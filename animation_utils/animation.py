from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

def step_slice(lst, idx):
    return lst[idx]

def animate_list(lst):
    return interact(step_slice,
                    lst=fixed(lst),
                    idx=widgets.IntSlider(min=0, max=len(lst)-1, step=1, value=0))

def step_dict(dct, key):
    return animate_list(dct[key]);

def animate_dict(dct, description=None):
    return interact(step_dict,
                    dct=fixed(dct),
                    key=widgets.Select(options=dct.keys(),
                                       description=description));