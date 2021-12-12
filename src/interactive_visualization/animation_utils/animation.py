from __future__ import print_function
from ipywidgets import interact, fixed
import ipywidgets as widgets
from IPython.display import display


def step_slice(lst, step):
    """
    Wrapper function that returns lst[step] value

    Args:
        lst: list to get value from
        step: index of the value

    Returns:
        value of list at step
    """
    return lst[step]


def animate_list(lst, play=False, navigation=True, interval=200):
    """
    Wrapper function that creates a widget with navigation over a list of visualization objects

    Args:
        lst: list of static visualization objects to navigate over
        play: if True, widget will contain basic audio like playbar
        navigation: if True, widget will contain prev and next buttons
        interval: if play=True, interval will set the delay between frame change (in ms)

    Returns:
        ipywidgets.interact object navigating over lst
    """
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
            display(play_widget)
        elif navigation:
            display(widgets.HBox([prev_button, next_button]))

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
