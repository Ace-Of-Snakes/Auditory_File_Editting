import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import time

def fs_synthesize (time_vals:np.ndarray, a_coeffs:np.ndarray ,b_coeffs:np.ndarray , T:float ) -> np . ndarray:
    """
    Diese Funktion berechnet den Fourier - Synthese - Algorithmus für ein
    gegebenes Zeitfenster und gibt das entsprechende Signal zurück .
    : param time_vals : ein numpy - Array mit den Zeitpunkten für die
    Berechnung des Signals
    : param a_coeffs : ein numpy - Array mit den a - Koeffizienten
    : param b_coeffs : ein numpy - Array mit den b - Koeffizienten
    : param T : die Periode des Signals
    : returns : ein numpy - Array mit den berechneten Signalwerten
    """
    x = np.zeros(len(time_vals))
    for k in range(len(a_coeffs)):
        if k == 0:
            x += a_coeffs[k]/2
        else:
            x += a_coeffs[k]*np.cos(2*np.pi*k*time_vals/T)
    for k in range(1, len(b_coeffs)):
        x += b_coeffs[k]*np.sin(2*np.pi*k*time_vals/T)
    return x

def sawtooth_demo():
    t_vals = np.linspace(-3,3,1000,endpoint= False )
    g_vals = signal.sawtooth(t_vals*np.pi+np.pi,1)

    # a_coeffs werden wie folgend berechnet
    a_coeffs = np.zeros_like(t_vals)

    # k ist die Anzahl der Koeffizienten die mit berechnet werden, je höher k desto genauer ist die Rekonstruktion
    # k ist unabhängig von den t_vals
    k = 1000
    # b_coeffs werden wie folgend berechnet
    b_coeffs = np.arange(1,k)
    b_coeffs = - (2*np.pi*b_coeffs*np.cos(np.pi*b_coeffs))/((np.pi**2)*(b_coeffs**2))
    b_coeffs = np.append([0],b_coeffs)

    g_reconstruct_vals = fs_synthesize(t_vals, a_coeffs, b_coeffs, 2)

    fig, ax = plt.subplots(2)
    ax[0].plot(t_vals, g_vals)
    ax[0].set_title("Original")
    ax[1].plot(t_vals, g_reconstruct_vals)
    ax[1].set_title("Reconstructed")

    plt.show()

def square_demo():
    t_vals = np.linspace(-6*np.pi,6*np.pi,1000,endpoint= False )
    g_vals = signal.square(t_vals*np.pi+np.pi)

    # k ist die Anzahl der Koeffizienten die mit berechnet werden, je höher k desto genauer ist die Rekonstruktion
    # k ist unabhängig von den t_vals
    k = 1000
    # a_coeffs werden wie folgend berechnet
    a_coeffs = np.arange(0,k)
    a_coeffs = 2*np.sin((np.pi*a_coeffs)/2)/(np.pi*a_coeffs)
    a_coeffs[0] = 1

    # b_coeffs werden wie folgend berechnet
    b_coeffs = np.zeros_like(t_vals)

    g_reconstruct_vals = fs_synthesize(t_vals, a_coeffs, b_coeffs, 2)

    fig, ax = plt.subplots(2)
    ax[0].plot(t_vals, g_vals)
    ax[0].set_title("Original")
    ax[1].plot(t_vals, g_reconstruct_vals)
    ax[1].set_title("Reconstructed")

    plt.show()

def periodically_continued(a, b):
    interval = b - a
    return lambda f: lambda x: f((x - a) % interval + a)


def periodic_func_demo():
    t_vals = np.linspace(0,6,1000,endpoint= False)

    @periodically_continued(0,2)
    def g(x):
        if x >= 0 and x < 1:
            return 1-x
        elif x >= 1 and x < 2:
            return -1

    g_vals = np.array([g(x) for x in t_vals])


    # k ist die Anzahl der Koeffizienten die mit berechnet werden, je höher k desto genauer ist die Rekonstruktion
    # k ist unabhängig von den t_vals
    k = 1000
    # a_coeffs werden wie folgend berechnet
    a_coeffs = np.arange(1,k)
    a_coeffs = -(np.cos(a_coeffs*np.pi)-1)/(a_coeffs**2*np.pi**2)
    a_coeffs = np.append([0],a_coeffs)
    a_coeffs[0] = -1/2

    # b_coeffs werden wie folgend berechnet
    b_coeffs = np.arange(1,k)
    b_coeffs = (2 - np.cos(b_coeffs*np.pi))/(b_coeffs*np.pi)
    b_coeffs = np.append([0],b_coeffs)

    g_reconstruct_vals = fs_synthesize(t_vals, a_coeffs, b_coeffs, 2)

    fig, ax = plt.subplots(2)
    ax[0].plot(t_vals, g_vals)
    ax[0].set_title("Original")
    ax[1].plot(t_vals, g_reconstruct_vals)
    ax[1].set_title("Reconstructed")

    plt.show()

def DFT(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(2j * np.pi * k * n / N)
    return np.dot(M, x)

def IDFT(X):
    N = len(X)
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, X) / N

if __name__ == "__main__":
    array = np.random.randint(0,10,5)

    print("Array: ", array)

    print(DFT(array))
    print(np.fft.fft(array))

    print(IDFT(array))
    print(np.fft.ifft(array))
    print(IDFT(DFT(array)))
    print(np.fft.ifft(np.fft.fft(array)))
    # sawtooth_demo()
    # square_demo()
    # periodic_func_demo()



