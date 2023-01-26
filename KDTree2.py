from scipy.spatial import cKDTree


class KDTree:
    """
    La classe KDTree è un wrapper per la classe cKDTree di scipy.spatial.
    Questa classe è stata creata per poter utilizzare la funzione query
    della classe cKDTree, che permette di trovare il punto più vicino
    ad un punto dato.
    """
    def __init__(self, points):
        self.tree = cKDTree(points)
        
    def find_nearest_neighbor(self, point):
        """
        Questo metodo permette di trovare il punto più vicino ad un punto dato.
        """
        dist, index = self.tree.query(point, p=2)
        return self.tree.data[index], dist

