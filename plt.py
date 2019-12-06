import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ColorConverter, ListedColormap, get_named_colors_mapping

DEFAULT_VMIN = 0
DEFAULT_VMAX = 1
DEFAULT_COLORMAP = 'hot'


def make_colormap(color):
    colors = [np.array(color) / 255 * i for i in range(256)]
    return ListedColormap(colors)


NAMED_COLORS = get_named_colors_mapping()
COLORS = [ColorConverter.to_rgb(NAMED_COLORS[color])
          for color in ('tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple',
                        'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan',
                        'lime', 'gold', 'indigo', 'w')]
COLORMAPS = [make_colormap(COLOR) for COLOR in COLORS]


def fuse_canals(im, colors=COLORS):
    new_im = np.zeros((im.shape[0], im.shape[1], 3))
    for x, line in enumerate(np.argmax(im, axis=-1)):
        for y, px in enumerate(line):
            new_im[x, y] = colors[px]
    return new_im


def imshow(im, cmap=DEFAULT_COLORMAP, vmin=DEFAULT_VMIN, vmax=DEFAULT_VMAX):
    if len(im.shape) == 2:
        plt.imshow(im, vmin=vmin, vmax=vmax, cmap=cmap)
    elif im.shape[2] == 1:
        plt.imshow(im[:, :, 0], vmin=vmin, vmax=vmax, cmap=cmap)
    elif im.shape[2] == 3:
        plt.imshow(im)
    else:
        im = fuse_canals(im)
        plt.imshow(im)