import matplotlib.pyplot as plt
from matplotlib import colors as mcolors

colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)

# Sort colors by hue, saturation, value and name.
by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name)
                for name, color in colors.items())
names = [name for hsv, name in by_hsv if name not in {'black', 'k', 'w', 'white', 'crimson', 'royalblue', 'limegreen', 'yellow', 'orange'}]
import random
random.shuffle(names)
names = ['crimson', 'royalblue', 'limegreen', 'yellow', 'orange', *names]
names.append('red')
names.append('white')
names.append('black')

def fill_cell(i, j, color, ax):
    ax.fill([i, i, i + 1, i + 1, i], [j, j + 1, j + 1, j, j], color=color)

def draw_filling(filling, horizonal_scale=0.75, vertical_scale=0.75):
    if filling is not None:
        n = len(filling)
        m = len(filling[0])
        fig = plt.figure(figsize=(m * vertical_scale, n * horizonal_scale))

        ax = fig.add_axes([0, 0, 1, 1])
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        for name, spine in ax.spines.items():
            spine.set_visible(False)
            spine.set_visible(False)

        for i, row in enumerate(filling):
            i = n - i - 1
            for j, cell in enumerate(row):
                fill_cell(j, i, names[cell], ax)

        for i in range(n + 1):
            ax.plot([0, m], [i, i], color='black')
        for i in range(m + 1):
            ax.plot([i, i], [0, n], color='black')
        plt.close(fig)
        return fig
    else:
        return None
