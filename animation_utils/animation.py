from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from IPython.display import display


def step_slice(lst, step):
    return lst[step]


def animate_list(lst, play=False, navigation=True, interval=200):
    slider = widgets.IntSlider(min=0, max=len(lst) - 1, step=1, value=0)
    
    if navigation:
        prev_button = widgets.Button(
                description='Prev',
                disabled=False,
            )
        next_button = widgets.Button(
                description='Next',
                disabled=False,
            )
        def increment_value(arg):
            slider.value += 1
        def decrement_value(arg):
            slider.value -= 1
            
        prev_button.on_click(decrement_value)
        next_button.on_click(increment_value)
    
    if play:
        play_widget = widgets.Play(interval=interval)
        widgets.jslink((play_widget, 'value'), (slider, 'value'))
        
    if play or navigation:
        if play and navigation:
            display(widgets.HBox([play_widget, prev_button, next_button]))
        elif play:
            display(play_widjet)
        elif navigation:
            display(HBox([prev_button, next_button]))
        
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
