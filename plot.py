import matplotlib as mpl
from matplotlib import pyplot as plt

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
    ax.set_xlabel(data[0][0].name)
    ax.set_ylabel(data[0][1].name)
    
    if proj == "3d":
        ax.set_zlabel(data[0][2][0])

    for x in range(len(data)):

        if plot_type == "line":
            plt.plot(*data[x], colours[x], label="Data %s" % (x))
            
        elif plot_type == "scatter":
            plt.scatter(*data[x], marker=".", c=colours[x],
                        label="Data %s" % (x))

    plt.legend()
    plt.show()
