import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from Lab1.utils import integer_generator_from_range

frames = 200
scope = (0, 10)
variables = np.arange(*scope)
occurrences = np.zeros(len(variables), dtype=int)
fig, ax = plt.subplots()

ax.set_xticks(variables)
ax.set_yticks(np.arange(0, 1, 0.1))
ax.set_ylabel('Probability')
ax.set_title('Probability of occurrence the variables in the uniform distribution.')
ax.set_ylim((0, 1))
ax.axhline(y=1 / len(variables), color='r', linestyle='-')

bars = ax.bar(variables, occurrences, align='center', alpha=0.5)


def init():
    for bar in bars:
        bar.set_height(0)


def animate(i):
    occurrences[next(integer_generator_from_range(*scope))] += 1
    probabilities = occurrences / np.sum(occurrences)
    for i, bar in enumerate(bars):
        bar.set_height(probabilities[i])


anim = animation.FuncAnimation(fig, animate, init_func=init, repeat=False, blit=False, frames=frames, interval=10)
plt.show()
