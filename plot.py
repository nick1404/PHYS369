import matplotlib as mpl
from matplotlib import pyplot as plt

# mpl.rc('text', usetex = True)
# mpl.rcParams['lines.linewidth'] = 6
# mpl.rcParams['axes.linewidth'] = 1.0
# mpl.rcParams['xtick.major.size'] = 9
# mpl.rcParams['xtick.minor.size'] = 5
# mpl.rcParams['xtick.major.width'] = 1.9
# mpl.rcParams['xtick.minor.width'] = 1.3
# mpl.rcParams['ytick.major.size'] = 9
# mpl.rcParams['ytick.minor.size'] = 4
# mpl.rcParams['ytick.major.width'] = 1.9
# mpl.rcParams['ytick.minor.width'] = 1.3


def plotstart(data, plot_type, x_label='x', y_label='y', dataset=[], x_err=None, y_err=None):

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
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    if proj == "3d":
        ax.set_zlabel(data[0][2][0])

    for x in range(len(data)):

        if plot_type == "line":
            plt.plot(*data[x], colours[x], label=dataset[x])
            
        elif plot_type == "scatter":
            plt.scatter(*data[x], marker=".", c=colours[x],
                        label=dataset[x])

        # if x_err:
        #     plt.errorbar(x=data[x][0], y=data[x][1],
        #                     xerr=x_err[x], c=colours[x], linestyle=None)
        # if y_err:
        #     plt.errorbar(x=data[x][0], y=data[x][1],
        #                     yerr=y_err[x], c=colours[x], linestyle=None)

    plt.tick_params(which='both', direction='in', right=True, top=True)
    plt.legend()
    plt.show()
