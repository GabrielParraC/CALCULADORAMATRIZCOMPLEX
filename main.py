import numpy as np


def addVec():
    arr1 = np.array([3 - 2j, 2j, 1 - 1j])
    arr2 = np.array([1 + 3j, 2 - 1j, 3 + 1j])
    s = np.add(arr1, arr2)
    print("Suma entre vectores:")
    print(s)
    print(" ")


def InverVec():
    arr1 = np.array([3 - 2j, 2j, 1 - 1j])
    inv = arr1 * -1
    print("Inverso aditivo de un vector:")
    print(inv)
    print(" ")


def EscVec():
    arr = np.array([1 - 2j, 2 + 3j, 3j])
    newarr = arr * 3
    print("Escalar por un vector:")
    print(newarr)
    print(" ")


def addMat():
    x = np.array([[1 + 2j, 4j, 7 - 2j], [2j, 5 - 3j, 8 + 1j], [3 - 2j, 6 + 3j, 9j]])
    y = np.array([[1 + 2j, 4j, 7 - 2j], [2j, 5 - 3j, 8 + 1j], [3 - 2j, 6 + 3j, 9j]])
    s = np.add(x, y)
    print("Suma entre matrices:")
    print(s)
    print(" ")


def InverMat():
    x = np.array([[1 + 2j, 4j, 7 - 2j], [2j, 5 - 3j, 8 + 1j], [3 - 2j, 6 + 3j, 9j]])
    inv = x * -1
    print("Inverso aditivo de un vector:")
    print(inv)
    print(" ")


def EscMat():
    x = np.array([[1 + 2j, 4j, 7 - 2j], [2j, 5 - 3j, 8 + 1j], [3 - 2j, 6 + 3j, 9j]])
    newarr = x * 3
    print("Escalar por una matriz:")
    print(newarr)
    print(" ")


def trans():
    x = np.array([[1 + 2j, 4j, 7 - 2j], [2j, 5 - 3j, 8 + 1j], [3 - 2j, 6 + 3j, 9j]])
    y = np.transpose(x)
    print("Trasnpuesta:")
    print(y)
    print(" ")



def producMat():
    A = np.array([[1 + 2j, 2j], [3j, 4 + 2j], [5 - 1j, 6 + 2j]])
    B = np.array([[1j, 2 - 2j, 3 + 2j], [3 - 1j, 4 + 3j, 5j]])
    result = np.dot(A, B)
    print("producto enter 2 matrices")
    print(result)
    print(" ")


def accion():
    a = np.array((1 + 2j, 2j, 3 + 3j))
    mat = np.array([[-1 - 1j, 1j, 0 + 2j],
                    [-4 - 1j, 3j, 0j],
                    [1 + 2j, 0 - 1j, 2 + 5j]])
    dotp = np.dot(mat, a)
    print("accion de matriz sobre un vector :")
    print(dotp)
    print(" ")


def productInt():
    a = np.array((1 + 2j, 2j, 3 + 3j))
    b = np.array((4 + 1j, 5j, 6 + 2j))
    dotp = np.dot(a, b)
    print("Producto interno:")
    print(dotp)
    print(" ")


def norma():
    vec = np.array([[1 + 2j, 2 + 1j, 3 - 1j]])
    vec_norm = np.linalg.norm(vec)
    print("Norma del vector:")
    print(vec_norm)
    print(" ")


def distancia():
    a = np.array((1 + 2j, 2j, 3 + 3j))
    b = np.array((4 + 1j, 5j, 6 + 2j))
    dist = np.linalg.norm(a - b)
    print("Distancia entre vectores:")
    print(dist)
    print(" ")


def valorprop():
    mat = np.array([[-1 - 1j, 1j, 0 + 2j],
                    [-4 - 1j, 3j, 0j],
                    [1 + 2j, 0 - 1j, 2 + 5j]])
    eigenvalue, featurevector = np.linalg.eig(mat)
    print("Valores propios:")
    print(eigenvalue)
    print(" ")
    print("Vectores propios:")
    print(featurevector)
    print(" ")




if __name__ == "__main__":
    valorprop()
    distancia()
    norma()
    productInt()
    accion()
    producMat()
    trans()
    EscMat()
    InverMat()
    addMat()
    EscVec()
    InverVec()
    addVec()
    
