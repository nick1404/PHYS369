import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import colors as mcolors
from mpl_toolkits import mplot3d


def plotstart(data, plot_type):
    if len(data[0]) > 3 or len(data[0]) < 2:
        print("Too much or not enough data!")
        return
    else:
        if len(data[0]) == 3:
            proj = "3d"
        else:
            proj = "rectilinear"

    colours = ["Red", "Blue", "Green", "Purple", "Orange",
               "Cyan", "Brown", "Olive", "Pink", "Gray", "Black"]

    font = {'family': 'arial',
            'weight': 'normal',
            'size': 10}

    mpl.rc('font', **font)

    plt.figure(dpi=200)

    ax = plt.axes(projection=proj)
    ax.set_xlabel(data[0][0][0])
    ax.set_ylabel(data[0][1][0])
    if proj == "3d":
        ax.set_zlabel(data[0][2][0])

    for x in range(len(data)):
        for y in range(len(data[x])):
            del data[x][y][0]

        if plot_type == "line":
            plt.plot(*data[x], colours[x], label="Data %s" % (x))
        elif plot_type == "scatter":
            plt.scatter(*data[x], marker=".", c=colours[x],
                        label="Data %s" % (x))

    plt.legend(loc="upper left")


data = [[["x", 1, 2, 3, 4, 5], ["y", 1, 2, 3, 4, 5], ["z", 1, 2, 3, 4, 5]],
        [["x", 5, 6, 7, 8, 9], ["y", 5, 6, 7, 8, 9], ["z", 5, 6, 7, 8, 9]]]

plotstart(data, "scatter")
plt.show()
