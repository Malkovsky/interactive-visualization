from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from IPython.display import display


def step_slice(lst, step):
    return lst[step]


def animate_list(lst, play=False, interval=200):
    slider = widgets.IntSlider(min=0, max=len(lst) - 1, step=1, value=0)
    if play:
        play_widjet = widgets.Play(interval=interval)
        widgets.jslink((play_widjet, 'value'), (slider, 'value'))
        display(play_widjet)
        # slider = widgets.Box([play_widject, slider])
    return interact(step_slice,
                    lst=fixed(lst),
                    step=slider)


def step_dict(dct, key):
    return animate_list(dct[key]);


def animate_dict(dct, description=None):
    return interact(step_dict,
                    dct=fixed(dct),
                    key=widgets.Select(options=dct.keys(),
                                       description=description));
