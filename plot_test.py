import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import colors as mcolors
from mpl_toolkits import mplot3d

def plotstart(data):
    if len(data[0]) > 3 or len(data[0]) < 2:
        print("Too much or not enough data!")
        return
    else:
        if len(data[0]) == 3:
            proj = "3d"
        else:
            proj = "rectilinear"
    
    colours=["Red","Blue","Green","Purple","Orange","Cyan","Brown","Olive","Pink","Gray","Black"]


    font = {'family': 'arial',
            'weight': 'normal',
            'size': 10}

    mpl.rc('font', **font)

    plt.figure(figsize=(99,54), dpi=200)

    ax = plt.axes(projection=proj)
    ax.set_xlabel(data[0][0][0])
    ax.set_ylabel(data[0][1][0])
    if proj == "3d":
        ax.set_zlabel(data[0][2][0])
    
    
    for x in range(len(data)):
        for y in range(len(data[x])):
            del data[x][y][0]

        plt.plot(*data[x], colours[x], label="Data %s" %(x))

    plt.legend(loc="upper left")

#plotstart([[["x",1,2,3,4,5],["y",1,2,3,4,5],["z",1,2,3,4,5]]])
#plotstart([[["x",1,2,3,4,5],["y",1,2,3,4,5]]])
#plt.show()