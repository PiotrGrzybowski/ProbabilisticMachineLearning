import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

from Lab1.utils import integer_generator_from_range

start = 0
stop = 5
occurrences = np.zeros((stop, stop))

fig, ax = plt.subplots()
data = np.random.rand(stop, stop)
im = ax.imshow(data, cmap=plt.get_cmap('hsv'))

ax.set_xlim(start-1, stop)
ax.set_ylim(start-1, stop)
numbers = []


def init():
    im.set_data(np.zeros((stop, stop)))
    numbers.append(next(integer_generator_from_range(start, stop)))
    return im


def animate(i):
    numbers.append(next(integer_generator_from_range(start, stop)))
    occurrences[numbers[-2]][numbers[-1]] += 1
    im.set_data(occurrences / np.sum(occurrences))
    return im


anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=100, repeat=False)
plt.show()
