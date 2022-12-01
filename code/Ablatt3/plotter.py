import numpy as np
import matplotlib.pyplot as plt
import math

def graph_settings():
    # setting the axes at the centre
    # only to be used when the graph is symmetric
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

def aufgabe1(save_im = False):
    # 100 linearly spaced numbers
    x = np.linspace(0, 2, 100,endpoint=False)

    # the function with the amplitude of 2 and of frequency 3Hz in Task1
    y = 2 * np.sin(6*math.pi*x)
    # 2 * np.sin(6*math.pi*x)

    # plot the function
    plt.plot(x,y, 'b-')

    if save_im:
          plt.savefig('plot_1.png')

    # show the plot
    plt.show()


def aufgabe2_1(save_im = False):
    # 600 linearly spaced numbers
    t = np.linspace(0, 3, 200*3,endpoint=False)

    # the function with the amplitude of 2 and of frequency 3Hz in Task1
    y = 3*np.cos(2*math.pi*t) + np.sin(4*math.pi*t) + np.cos(6*math.pi*t)

    if save_im:
          plt.savefig('plot_1.png')
    
    # plot the function
    plt.plot(t,y, 'b-')

    # show the plot
    plt.show()


def aufgabe2_2(save_im = False,justReturn = False):
     # 30 linearly spaced numbers
    fs = 10
    t = np.linspace(0, 3, fs*3,endpoint=False)
    t2 = np.linspace(0, 3, 600,endpoint=False)
    # the function with the amplitude of 2 and of frequency 3Hz in Task1
    y = 3*np.cos(2*math.pi*t) + np.sin(4*math.pi*t) + np.cos(6*math.pi*t)
    y2 = 3*np.cos(2*math.pi*t2) + np.sin(4*math.pi*t2) + np.cos(6*math.pi*t2)
    
    if justReturn:
        return t,t2,y,y2
    else:    
        # plot the function
        plt.stem(t,y, 'b-')
        plt.plot(t2,y2, 'r-')
    if save_im:
        plt.savefig('AbildAufgabe2_2.png')
    else:
        # show the plot
        plt.show()


def reconstruct (sample_vals : np.ndarray , fs : int , t_vals : np.ndarray) -> np.ndarray:
    
    y = np.zeros(t_vals.shape)
    T=1/fs

    for i in range(len(sample_vals)):
        y += sample_vals[i] * np.sinc((t_vals-i*T)/T)
    return y

def aufgabe2_3(save_im = False):
# using the function from the task 2.2
    # 600 linearly spaced numbers
    fs = 6
    t = np.linspace(0, 3, fs*3,endpoint=False)
    # the function with the amplitude of 2 and of frequency 3Hz in Task1

    sample_vals = 3*np.cos(2*math.pi*t) + np.sin(4*math.pi*t) + np.cos(6*math.pi*t)
    t_vals = np.linspace(0,3,600)

    y = reconstruct(sample_vals, fs, t_vals)
    # print(y)
   

    # plot the function
    x,x2,z,z2=aufgabe2_2(False,True)
    plt.plot(t_vals,y)
    plt.stem(x,z)
    plt.plot(x2,z2, 'r-')
    # show the plot
    if save_im:
          plt.savefig('ABild233.png')
    plt.show()

if __name__=="__main__":
    aufgabe1()
    aufgabe2_1()
    aufgabe2_2()
    aufgabe2_3()
    exit()
