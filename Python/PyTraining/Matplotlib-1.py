#Matplotlib
#Library for graph/plot visualization


import matplotlib.pyplot as plt
import numpy as np

l1 = [0, 5]
l2 = [0, 100]

def simple_line_plot(l1, l2):
    x = np.array(l1)
    y = np.array(l2)

    plt.plot(x, y)

    plt.title("Data")
    plt.xlabel("Label-One")
    plt.ylabel("Label-Two")

    plt.grid()   #optional - if grid lines required we can call this

    plt.show()

simple_line_plot(l1, l2)

def simple_ring_plot(l1, l2):
    x = np.array(l1)
    y = np.array(l2)

    plt.plot(x, y, 'o')   #plotting without lines, third parameter here means rings
    plt.show()

#simple_ring_plot(l1, l2)

def multi_point_plot(l1, l2):
    x = np.array(l1)
    y = np.array(l2)

    plt.plot(x, y)   
    plt.show()


l1 = [1, 2, 4, 8]
l2 = [3, 8, 2, 12]


#multi_point_plot(l1, l2)

#value are given only for one direction
def multi_point_plot2(l2):
    y = np.array(l2)

    plt.plot(y)   
    plt.show()


#multi_point_plot2(l2)


def plot_with_marker(l2, mark):
    y = np.array(l2)

    plt.plot(y, marker= mark)   
    plt.show()


#plot_with_marker(l2, "o")  #circle
#plot_with_marker(l2, "*") #Star
#plot_with_marker(l2, "+") #plus
#plot_with_marker(l2, "s") #square
#plot_with_marker(l2, "D") #diamond


def multi_point_plot3(l1, l2, fmt, markerSize=5):
    x = np.array(l1)
    y = np.array(l2)

    plt.plot(x, y, fmt, markerSize)   
    plt.show()


#multi_point_plot3(l1, l2, 'o:g')   # o = circle marker, : = dotted lines, g = green color

#multi_point_plot3(l1, l2, 'D--m')  # o = Diamond marker, -- = dashed lines, g = Magenta color

#multi_point_plot3(l1, l2, '*-.r')  # o = star marker, -. = dash and dotted lines, g = red color



def multi_point_plot4(l1, l2, mark, markerSize=5):
    x = np.array(l1)
    y = np.array(l2)

    plt.plot(x, y, marker =mark, ms = markerSize)   
    plt.show()


#multi_point_plot4(l1, l2, 'o')
#multi_point_plot4(l1, l2, '*', 25)


l1 = [1, 2, 4, 8]
l2 = [3, 8, 2, 12]
l3 = [0, 1, 2, 3]
l4 = [2, 4, 6, 8]

def multi_coordinates_line_plot(l1, l2, l3, l4):
    x1 = np.array(l1)
    y1 = np.array(l2)

    x2 = np.array(l3)
    y2 = np.array(l4)

    plt.plot(x1, y1, x2, y2)   
    plt.show()


#multi_coordinates_line_plot(l1, l2, l3, l4)


values = [15, 25, 35, 20, 30]
labels = ["Football", "Cricket", "Tennis", "Badminton", "Others"]


def pie_plot(data, label, explode=True):
    y = np.array(data)

    exp = [0, 0, 0.2, 0, 0.1]

    if explode:
        plt.pie(y, labels=label, explode=exp)   
    else:
        plt.pie(y, labels=label)   
        plt.legend()
    plt.show()


pie_plot(values, labels, False)
pie_plot(values, labels)