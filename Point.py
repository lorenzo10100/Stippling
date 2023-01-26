import numpy as np 

class Point:
    """
    La classe Point è una classe che rappresenta un punto all'interno dell'immagine
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def __str__(self):
        """
        questo metodo permette di stampare un punto in un formato leggibile
        """
        return "Point(%s, %s)" % (self.x, self.y)

    @classmethod
    def __repr__(self):
        """
        questo metodo permette di stampare un punto in un formato leggibile
        """
        return self.__str__()

    @classmethod
    def getDistance(self, other):
        """
        questo metodo permette di calcolare la distanza tra due punti
        """
        return np.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

def sortByX(array):
    """
    questa funzione permette di ordinare un array di punti in base alla coordinata x
    """
    return sorted(array, key=lambda point: point.x)
    
def sortByY(array):
    """
    questa funzione permette di ordinare un array di punti in base alla coordinata y
    """
    return sorted(array, key=lambda point: point.y)
