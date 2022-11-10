import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.animation as animation
import numpy as np
from matplotlib.animation import FuncAnimation


def createAnimation(mytrace, trueValues, stages, labelsName, thetachoice):
    fig = plt.figure()
    plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams["font.size"] = 12
    ax = plt.axes(projection='3d')
    ax.set_xlim3d(0.0e9, 2e9)
    ax.set_ylim3d(0.0e9, 2e9)
    ax.set_zlim3d(0.0e9, 2e9)
    sct, = ax.plot([], [], [], ".", color='b', alpha=0.2)
    plt.plot(trueValues[1], trueValues[0], trueValues[0], 'ro', label='True')
    def animate(i):
        Sm = mytrace[i][0]
        Wm = mytrace[i][2]
        sct.set_data(Sm[:, thetachoice[0]], Sm[:, thetachoice[1]])
        sct.set_3d_properties(Sm[:, thetachoice[2]])
        return sct,

    ax.set_xlabel(labelsName[0])
    ax.set_ylabel(labelsName[1])
    ax.set_zlabel(labelsName[2])
    plt.legend()
    anim = animation.FuncAnimation(fig, animate, frames=len(stages),
                                   interval=1000, blit=True)

    # saving to m4 using ffmpeg writer

    # writervideo = animation.FFMpegWriter(fps=60)
    path = 'increasingStraightLine.gif'

    anim.save(path, writer='PillowWriter', fps=80)