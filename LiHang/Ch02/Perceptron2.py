# -*- coding:utf-8 -*-
# Filename: train2.2.py
# Author：hankcs
# Date: 2015/1/31 15:15
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
 
# An example in that book, the training set and parameters' sizes are fixed
# training_set = np.array([[[3, 3], 1], [[4, 3], 1], [[1, 1], -1]])
training_set = np.array([[[3, 3], 1], [[4, 3], 1], [[1, 1], -1], [[5, 2], -1]])
 
a = np.zeros(len(training_set), np.float)
b = 0.0
Gram = None
y = np.array(training_set[:, 1])
x = np.empty((len(training_set), 2), np.float)
for i in range(len(training_set)):
    x[i] = training_set[i][0]
history = []
 
def cal_gram():
    """
    calculate the Gram matrix
    :return:
    """
    g = np.empty((len(training_set), len(training_set)), np.int)
    for i in range(len(training_set)):
        for j in range(len(training_set)):
            g[i][j] = np.dot(training_set[i][0], training_set[j][0])
    return g
 
 
def update(i):
    """
    update parameters using stochastic gradient descent
    :param i:
    :return:
    """
    global a, b
    a[i] += 1
    b = b + y[i]
    history.append([np.dot(a * y, x), b])
    # print a, b # you can uncomment this line to check the process of stochastic gradient descent
 
 
# calculate the judge condition
def cal(i):
    global a, b, x, y
 
    res = np.dot(a * y, Gram[i])
    res = (res + b) * y[i]
    return res
 
 
# check if the hyperplane can classify the examples correctly
def check():
    global a, b, x, y
    flag = False
    for i in range(len(training_set)):
        if cal(i) <= 0:
            flag = True
            update(i)
    if not flag:
 
        w = np.dot(a * y, x)
        print "RESULT: w: " + str(w) + " b: " + str(b)
        return False
    return True
 
 
if __name__ == "__main__":
    Gram = cal_gram()  # initialize the Gram matrix
    for i in range(1000):
        if not check(): break
 
    # draw an animation to show how it works, the data comes from history
    # first set up the figure, the axis, and the plot element we want to animate
    fig = plt.figure()
    ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
    line, = ax.plot([], [], 'g', lw=2)
    label = ax.text([], [], '')
 
    # initialization function: plot the background of each frame
    def init():
        line.set_data([], [])
        x, y, x_, y_ = [], [], [], []
        for p in training_set:
            if p[1] > 0:
                x.append(p[0][0])
                y.append(p[0][1])
            else:
                x_.append(p[0][0])
                y_.append(p[0][1])
 
        plt.plot(x, y, 'bo', x_, y_, 'rx')
        plt.axis([-6, 6, -6, 6])
        plt.grid(True)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Perceptron Algorithm 2 (www.hankcs.com)')
        return line, label
 
 
    # animation function.  this is called sequentially
    def animate(i):
        global history, ax, line, label
 
        w = history[i][0]
        b = history[i][1]
        if w[1] == 0: return line, label
        x1 = -7.0
        y1 = -(b + w[0] * x1) / w[1]
        x2 = 7.0
        y2 = -(b + w[0] * x2) / w[1]
        line.set_data([x1, x2], [y1, y2])
        x1 = 0.0
        y1 = -(b + w[0] * x1) / w[1]
        label.set_text(str(history[i][0]) + ' ' + str(b))
        label.set_position([x1, y1])
        return line, label
 
    # call the animator.  blit=true means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(history), interval=1000, repeat=True,
                                   blit=True)
    plt.show()
    # anim.save('perceptron2.gif', fps=2, writer='imagemagick')
    