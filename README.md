# Python examples

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Malkovsky/python-examples/master)

This repository contains some material from different computer science topics in a form of jupyter notebooks. The core feature of the presentation from is vast use of automatically generated animated examples.

## Text animations

Here's an example of quicksort algorithm using text state representation

![Quicksort](https://raw.githubusercontent.com/Malkovsky/python-examples/master/images/quicksort.gif)

## Matplotlib animations

Using `matplotlib` one can visualize some plane algorithm, for example [EM algorithm for Old Faithfull eruption data](https://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm)

![em](https://raw.githubusercontent.com/Malkovsky/python-examples/master/images/em_gmm.gif)

or domino coloring based on 5-coloring algorithm for planar graphs

![coloring](https://raw.githubusercontent.com/Malkovsky/python-examples/master/images/planar_coloring.gif)

or convex hull construction

![convex_hull](https://raw.githubusercontent.com/Malkovsky/python-examples/master/images/convex_hull.gif)

## Graphviz

Using `graphviz` one can visualize basic graph algorithms, here's an example of Dijkstra algorithm

![dijkstra](https://raw.githubusercontent.com/Malkovsky/python-examples/master/images/dijkstra_slow.gif)

# Requirements and prerequisites

Main visualization tools are `matplotlib` and `graphviz`, they can be installed manually or as
```
pip install -r requirements.txt
```
The other core component for most of the animated examples is [ipywidgets](https://ipywidgets.readthedocs.io/en/stable/user_install.html), check the docs for installation instractions, note that currently there might be problems when using widgets in jupyter lab.


# Table of content
## Eng
### [Linear programming](https://github.com/Malkovsky/python-examples/blob/master/lp_overview.ipynb)
Introduction to linear programming, simplex method and interior point method. Some animations are presented in [this notebook](https://github.com/Malkovsky/python-examples/blob/master/old_ani.ipynb) including ellipsoid method.
### [Gradient descent with momentum](https://github.com/Malkovsky/python-examples/blob/master/grad_ani.ipynb)
Compararison between different gradient momentum methods for a basic quadratic function. Currently code and animations only.
### [Paths on rectangles (junk)](https://github.com/Malkovsky/python-examples/blob/master/paths_on_rectangle.ipynb)
Some exdamples of probability walk on rectangular grid.
### [Covid-19](https://github.com/Malkovsky/python-examples/blob/master/covid19.ipynb)
Some basic parse and analysis of global Covid-19 data from Johns Hopkins University.
## Rus
### [Замощене доминошками](https://github.com/Malkovsky/python-examples/blob/master/domino_tiling.ipynb)
Рассматривается задача покрытия фигур на плоскости, состоящиех из квадратных клеток одинакового размера и два её программных решения: с помощью динамического программирования по профилю и с помощью нахождения максимального паросочетания. Бонусом идет раскраска планарного графа в 5 цветов (не протестировано).
### [Обходы на графх](https://github.com/Malkovsky/python-examples/blob/master/basic_searches.ipynb)
Разобраны обходы в глубину и ширину, а так же их базовые применения.
### [Кратчайшие пути на графах](https://github.com/Malkovsky/python-examples/blob/master/shortest_paths.ipynb)
Основные алгоритмы для задачи о крайших путях от одной вершины до всех остальных. Все алгоритмы представлены как модификации "сканирующего метода".
### [Префиксное дерево](https://github.com/Malkovsky/python-examples/blob/master/preffix_tree.ipynb)
Префиксное дерево, префикс-функцию, алгоритм Ахо-Корасик и их применения в марковских моделях для обработки текста.
