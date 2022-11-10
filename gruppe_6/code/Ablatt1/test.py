import numpy as np 

def welcome(message):
    print(message)

def array_magic(dim):
    random_array = np.random.randint(0,10, dim)
    return random_array

if __name__=="__main__":
    welcome('Willkommen im Praktikum Audiosignalverarbeitung')
    print(array_magic((2,3)))