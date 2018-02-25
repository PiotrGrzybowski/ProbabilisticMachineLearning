# import numpy as np
# from matplotlib import pyplot as plt
# from matplotlib import animation
#
# from Lab1.utils import integer_generator_from_range
#
# start = 0
# stop = 10
#
# fig = plt.figure()
# occurrences = np.zeros((stop, stop))
# im = plt.imshow(occurrences, cmap=plt.get_cmap('plasma'))
#
#
# def init():
#     im.set_data(np.zeros((start, stop)))
#
#
# def animate(i):
#     first = next(integer_generator_from_range(start, stop))
#     second = next(integer_generator_from_range(start, stop))
#     occurrences[first][second] += 1
#     im.set_data(occurrences)
#     return im
#
#
# anim = animation.FuncAnimation(fig, animate, init_func=init, frames=50, repeat=False)
# plt.show()

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

nx = 10
ny = 10
start = 0
stop = 10

fig = plt.figure()
data = np.random.rand(nx, ny)
im = plt.imshow(data, cmap=plt.get_cmap('plasma'))


def init():
    im.set_data(np.zeros((nx, ny)))


def animate(i):
    # xi = i // ny
    # yi = i % ny
    data = np.random.rand(nx, ny)
    im.set_data(data)
    return im


anim = animation.FuncAnimation(fig, animate, init_func=init, frames=50, repeat=False)
plt.show()
